import os
import sys
import re
import importlib
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel, ttk
from PIL import Image, ImageTk, ImageFilter
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

# ─── Ajuste PYTHONPATH ─────────────────────────────────────────────
base_dir    = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(base_dir, os.pardir))
sys.path.insert(0, base_dir)
sys.path.insert(0, project_dir)

# ─── ErrorListener para ANTLR ───────────────────────────────────────
class SintaxisListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"Línea {line}:{column} → {msg}")

def analizar_sintactico_antlr(codigo, lenguaje):
    parsers = {
        "Python":     ("PythonLexer",     "PythonParser"),
        "T-SQL":      ("TSQLLexer",       "TSQLParser"),
        "C++":        ("CPPLexer",        "CPPParser"),
        "JavaScript": ("JavaScriptLexer", "JavaScriptParser"),
        "Pascal":     ("PascalLexer",     "PascalParser"),
        "PL/SQL":     ("PLSQLLexer",      "PLSQLParser"),
        "HTML":       ("HTMLLexer",       "HTMLParser"),
    }
    if lenguaje not in parsers:
        return [f"❌ No hay parser ANTLR para {lenguaje}"]
    lx, ps = parsers[lenguaje]
    try:
        lex_mod = importlib.import_module(f"parser.grammar.{lx}")
        par_mod = importlib.import_module(f"parser.grammar.{ps}")
        Lexer  = getattr(lex_mod, lx)
        Parser = getattr(par_mod, ps)
    except Exception as e:
        return [f"❌ Error cargando ANTLR para {lenguaje}: {e}"]

    stream = InputStream(codigo)
    lexer  = Lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = Parser(tokens)

    listener = SintaxisListener()
    parser.removeErrorListeners()
    parser.addErrorListener(listener)
    try:
        if hasattr(parser, "program"):
            parser.program()
        elif hasattr(parser, "start"):
            parser.start()
    except Exception as e:
        listener.errores.append(str(e))

    return listener.errores

# ─── Módulos propios ────────────────────────────────────────────────
from lexer            import analizar_lexico
from detector_lenguaje import detectar_lenguaje
from semantic         import analizar_semantico
from tree_builder     import generar_arbol

# ─── Interfaz gráfica ───────────────────────────────────────────────
class SimuladorCompiladorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⚙️ SynthaCore - V5.5")
        self.root.geometry("1400x800")
        self.root.configure(bg="#1e1e1e")

        # ─── Canvas de fondo ─────────────────────────────────────────
        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # ─── Cargo imagen original ───────────────────────────────────
        self.bg_path = os.path.join(base_dir, "fondo_compilador.png")
        if os.path.exists(self.bg_path):
            self._bg_orig = Image.open(self.bg_path).convert("RGBA")
        else:
            self._bg_orig = None
            messagebox.showwarning("Aviso", f"No encontré fondo:\n{self.bg_path}")

        # ─── Ventana interna ─────────────────────────────────────────
        self.container = tk.Frame(self.canvas, bg="#1e1e1e")
        self._win = self.canvas.create_window(0, 0, anchor="nw", window=self.container)

        # ─── Bind resize ─────────────────────────────────────────────
        self.root.bind("<Configure>", self._on_resize)

        # ─── Construyo UI ───────────────────────────────────────────
        self._build_ui()

        # Inicializo datos
        self.tokens     = []
        self.lex_err    = []
        self.sint_err   = []
        self.sem_err    = []
        self.ruta_imagen = None

    def _build_ui(self):
        c = self.container

        # ── Botonera ───────────────────────────────────────────────
        botones = [
            ("▶️ Analizar",           "#00b894", self.analizar_codigo),
            ("📂 Cargar .txt",        "#0984e3", self.cargar_archivo),
            ("💾 Guardar resultado",  "#fdcb6e", self.guardar_resultado),
            ("🧹 Limpiar todo",       "#d63031", self.limpiar),
            ("🌳 Ver árbol completo", "#6c5ce7", self.abrir_arbol_ampliado),
            ("📊 Ver Tablas",         "#e17055", self.mostrar_tablas),
        ]
        fr = tk.Frame(c, bg="#1e1e1e")
        fr.grid(row=0, column=0, columnspan=2, pady=15)
        for txt, col, cmd in botones:
            b = tk.Button(fr, text=txt, command=cmd,
                          font=("Segoe UI",12), bg=col, fg="white",
                          bd=0, relief="flat", padx=10, pady=5)
            b.pack(side="left", padx=5)
            b.bind("<Enter>", lambda e,c=col: e.widget.config(bg="white", fg="#1e1e1e"))
            b.bind("<Leave>", lambda e,c=col: e.widget.config(bg=c, fg="white"))

        # ── Layout ────────────────────────────────────────────────
        c.grid_columnconfigure(0, weight=1)
        c.grid_columnconfigure(1, weight=1)
        c.grid_rowconfigure(1, weight=3)
        c.grid_rowconfigure(2, weight=2)

        # ── Código de entrada ─────────────────────────────────────
        f1 = tk.LabelFrame(c, text="📝 Código de entrada",
                           fg="white", bg="#1e1e1e",
                           font=("Segoe UI",12,"bold"), bd=0, relief="flat")
        f1.grid(row=1, column=0, rowspan=2, sticky="nsew", padx=20, pady=20)
        self.texto_entrada = tk.Text(f1, bg="#2d2d2d", fg="white",
                                     insertbackground="white",
                                     font=("Fira Code",12), bd=0, relief="flat")
        self.texto_entrada.pack(fill="both", expand=True, padx=5, pady=5)
        self.texto_entrada.bind("<KeyRelease>", self._expandir_textarea)

        # ── Resultado ─────────────────────────────────────────────
        f2 = tk.LabelFrame(c, text="📋 Resultado del análisis",
                           fg="white", bg="#1e1e1e",
                           font=("Segoe UI",12,"bold"), bd=0, relief="flat")
        f2.grid(row=1, column=1, sticky="nsew", padx=10, pady=(20,5))
        self.resultado_texto = tk.Text(f2, bg="#2d2d2d", fg="white",
                                       insertbackground="white",
                                       font=("Fira Code",12), bd=0, relief="flat")
        self.resultado_texto.pack(fill="both", expand=True, padx=5, pady=5)
        self.resultado_texto.bind("<KeyRelease>", self._expandir_resultado)

        # ── Consola ───────────────────────────────────────────────
        f3 = tk.LabelFrame(c, text="🧪 Consola de ejecución",
                           fg="white", bg="#1e1e1e",
                           font=("Segoe UI",12,"bold"), bd=0, relief="flat")
        f3.grid(row=2, column=1, sticky="nsew", padx=10, pady=(5,20))
        self.consola = tk.Text(f3, bg="#2d2d2d", fg="#00ff00",
                               insertbackground="#00ff00",
                               font=("Fira Code",11), bd=0, relief="flat")
        self.consola.pack(fill="both", expand=True, padx=5, pady=5)

        # ── Imagen del árbol ──────────────────────────────────────
        self.imagen_arbol = tk.Label(f2, bg="#1e1e1e")
        self.imagen_arbol.pack(pady=5)

        # Dibujo inicial del fondo
        self._draw_bg()

    def _on_resize(self, evt):
        w, h = self.root.winfo_width(), self.root.winfo_height()
        self.canvas.coords(self._win, 0, 0)
        self.canvas.itemconfigure(self._win, width=w, height=h)
        self._draw_bg()

    def _draw_bg(self):
        if not self._bg_orig:
            return
        w, h = self.root.winfo_width(), self.root.winfo_height()
        if w < 10 or h < 10:
            return
        img = self._bg_orig.resize((w, h), Image.LANCZOS)
        img = img.filter(ImageFilter.GaussianBlur(4))
        alpha = Image.new("L", img.size, 100)
        img.putalpha(alpha)
        self._bg_imgtk = ImageTk.PhotoImage(img)
        self.canvas.delete("bg")
        self.canvas.create_image(0, 0, anchor="nw",
                                 image=self._bg_imgtk, tags="bg")
        self.canvas.tag_lower("bg")

    def _expandir_textarea(self, e=None):
        lines = int(self.texto_entrada.index('end-1c').split('.')[0])
        self.texto_entrada.config(height=min(max(lines,1),20))

    def _expandir_resultado(self, e=None):
        lines = int(self.resultado_texto.index('end-1c').split('.')[0])
        self.resultado_texto.config(height=min(max(lines,1),25))

    def analizar_codigo(self):
        codigo = self.texto_entrada.get("1.0", tk.END).strip()
        if not codigo:
            return messagebox.showwarning("Advertencia", "Ingresa código.")

        # Léxico
        self.tokens, self.lex_err = analizar_lexico(codigo)
        # Sintáctico / Semántico
        lang = detectar_lenguaje(codigo)
        self.sint_err = []
        self.sem_err  = []
        if not self.lex_err:
            self.sint_err = analizar_sintactico_antlr(codigo, lang)
        if lang == "Python" and not self.lex_err:
            self.sem_err = analizar_semantico(codigo)

        # Texto de resultado
        txt = (
            f"Lenguaje: {lang}\n\n"
            f"Tokens:\n" + "".join(f"  [{t}]→{v}\n" for t,v in self.tokens) + "\n\n"
            f"Errores Léxicos:\n" +
              ( "\n".join(f"⚠️ {e}" for e in self.lex_err) if self.lex_err else "✅ Ninguno") + "\n\n"
            f"Errores Sintácticos:\n" +
              ( "\n".join(f"❌ {e}" for e in self.sint_err) if self.sint_err else "✅ Ninguno") + "\n\n"
            f"Errores Semánticos:\n" +
              ( "\n".join(f"⚠️ {e}" for e in self.sem_err) if self.sem_err else "✅ Ninguno")
        )
        self.resultado_texto.delete("1.0", tk.END)
        self.resultado_texto.insert(tk.END, txt)

        # Sólo genero el árbol si NO hay errores sintácticos
        if not self.sint_err:
            try:
                self.ruta_imagen = generar_arbol(codigo)
                img = Image.open(self.ruta_imagen).resize((600,300))
                self._imgtk = ImageTk.PhotoImage(img)
                self.imagen_arbol.config(image=self._imgtk)
            except SyntaxError as e:
                self.sint_err.append(str(e))
                self.imagen_arbol.config(image="")
                self.ruta_imagen = None
        else:
            self.imagen_arbol.config(image="")
            self.ruta_imagen = None

        # Simulación en consola
        out = ""
        if lang=="Python" and "print(" in codigo:
            for m in re.findall(r'print\((.*?)\)', codigo):
                out += f"🖨️ {m}\n"
        elif lang=="T-SQL" and "CREATE TABLE" in codigo.upper():
            out = "📦 Tabla creada\n"
        else:
            out = "ℹ️ Nada que ejecutar.\n"
        self.consola.delete("1.0", tk.END)
        self.consola.insert(tk.END, out)

    def mostrar_tablas(self):
        win = Toplevel(self.root)
        win.title("📊 Tablas de Análisis")
        win.geometry("1000x600")
        win.configure(bg="#1e1e1e")

        frm = tk.Frame(win, bg="#1e1e1e")
        frm.pack(fill="both", expand=True, padx=10, pady=10)
        frm.grid_columnconfigure((0,1), weight=1)
        frm.grid_rowconfigure((0,1), weight=1)

        def mk_frame(r,c,tit):
            lf = tk.LabelFrame(frm, text=tit, fg="white", bg="#1e1e1e",
                               font=("Segoe UI",11,"bold"), bd=0, relief="flat")
            lf.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
            return lf

        # Tokens
        lf1 = mk_frame(0,0,"🪙 Tokens")
        tv1 = ttk.Treeview(lf1, columns=("Tipo","Valor"), show="headings")
        tv1.heading("Tipo", text="Tipo"); tv1.heading("Valor", text="Valor")
        for t,v in self.tokens: tv1.insert("", "end", values=(t,v))
        tv1.pack(fill="both", expand=True)

        # Errores Léxicos
        lf2 = mk_frame(0,1,"⚠️ Errores Léxicos")
        tv2 = ttk.Treeview(lf2, columns=("Idx","Mensaje"), show="headings")
        tv2.heading("Idx", text="#"); tv2.heading("Mensaje", text="Mensaje")
        for i,e in enumerate(self.lex_err,1): tv2.insert("", "end", values=(i,e))
        tv2.pack(fill="both", expand=True)

        # Errores Sintácticos
        lf3 = mk_frame(1,0,"❌ Errores Sintácticos")
        tv3 = ttk.Treeview(lf3, columns=("Loc","Mensaje"), show="headings")
        tv3.heading("Loc", text="Línea:Col"); tv3.heading("Mensaje", text="Mensaje")
        for err in self.sint_err:
            parts = err.split("  ",1)
            loc,msg = (parts if len(parts)==2 else ("-",parts[0]))
            tv3.insert("", "end", values=(loc,msg))
        tv3.pack(fill="both", expand=True)

        # Errores Semánticos
        lf4 = mk_frame(1,1,"⚠️ Errores Semánticos")
        tv4 = ttk.Treeview(lf4, columns=("Idx","Mensaje"), show="headings")
        tv4.heading("Idx", text="#"); tv4.heading("Mensaje", text="Mensaje")
        for i,m in enumerate(self.sem_err,1): tv4.insert("", "end", values=(i,m))
        tv4.pack(fill="both", expand=True)

    def abrir_arbol_ampliado(self):
        if not self.ruta_imagen:
            return messagebox.showinfo("Info","Genera primero el árbol.")
        top = Toplevel(self.root)
        img = Image.open(self.ruta_imagen)
        w,h = img.size
        top.geometry(f"{w+20}x{h+20}")
        cv = tk.Canvas(top, width=w, height=h, bg="#1e1e1e")
        cv.pack()
        it = ImageTk.PhotoImage(img)
        cv.create_image(0,0,anchor="nw", image=it)
        cv.image = it

    def cargar_archivo(self):
        p = filedialog.askopenfilename(filetypes=[("TXT","*.txt")])
        if p:
            self.texto_entrada.delete("1.0", tk.END)
            self.texto_entrada.insert(tk.END, open(p, encoding="utf-8").read())

    def guardar_resultado(self):
        txt = self.resultado_texto.get("1.0", tk.END).strip()
        if not txt:
            return messagebox.showwarning("Advertencia","No hay qué guardar.")
        p = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("TXT","*.txt")])
        if p:
            with open(p,"w",encoding="utf-8") as f:
                f.write(txt)

    def limpiar(self):
        self.texto_entrada.delete("1.0", tk.END)
        self.resultado_texto.delete("1.0", tk.END)
        self.consola.delete("1.0", tk.END)
        self.imagen_arbol.config(image="")
        self.ruta_imagen = None

# ─── Arranque de la aplicación ───────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    SimuladorCompiladorApp(root)
    root.mainloop()