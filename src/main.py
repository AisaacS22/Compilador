# src/main.py

import os
import sys
import re
import importlib
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel, ttk
from tkinter import filedialog, messagebox, Toplevel
from PIL import Image, ImageTk, ImageFilter
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

# ─── Ajuste PYTHONPATH para src/ y parser/ ─────────────────────────────
base_dir    = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(base_dir, os.pardir))
sys.path.insert(0, base_dir)
sys.path.insert(0, project_dir)

# ─── ErrorListener común ───────────────────────────────────────────────
class SintaxisListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"Línea {line}:{column} → {msg}")

# ─── Función dinámica de ANTLR ────────────────────────────────────────
def analizar_sintactico_antlr(codigo, lenguaje):
    # Mapeo de nombres de módulos y clases
    info = {
        "Python":      ("PythonLexer",      "PythonParser"),
        "T-SQL":       ("TSQLLexer",        "TSQLParser"),
        "C++":         ("CPPLexer",         "CPPParser"),
        "JavaScript":  ("JavaScriptLexer",  "JavaScriptParser"),
        "Pascal":      ("PascalLexer",      "PascalParser"),
        "PL/SQL":      ("PLSQLLexer",       "PLSQLParser"),
        "HTML":        ("HTMLLexer",        "HTMLParser"),
    }
    if lenguaje not in info:
        return [f"❌ No hay parser ANTLR para {lenguaje}"]
    lexer_name, parser_name = info[lenguaje]
    try:
        lex_mod    = importlib.import_module(f"parser.grammar.{lexer_name}")
        pars_mod   = importlib.import_module(f"parser.grammar.{parser_name}")
        LexerClass = getattr(lex_mod, lexer_name)
        ParserClass= getattr(pars_mod, parser_name)
    except (ModuleNotFoundError, AttributeError) as e:
        return [f"❌ Error cargando ANTLR para {lenguaje}: {e}"]

    # Ejecutar ANTLR
    input_stream = InputStream(codigo)
    lexer  = LexerClass(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ParserClass(tokens)

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

# ─── Interfaz gráfica ─────────────────────────────────────────────────

class SimuladorCompiladorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⚙️ SynthaCore - V5.5")
        self.root.geometry("1400x800")
        self.root.configure(bg="#1e1e1e")

        # Canvas de fondo
        self.canvas = tk.Canvas(root, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bg_path = os.path.join(project_dir, "fondo_compilador.png")
        self.root.bind("<Configure>", self._redibujar_fondo)

        # Contenedor principal con grid
        container = tk.Frame(self.canvas, bg="#1e1e1e")
        container.place(relwidth=1, relheight=1)
        container.grid_columnconfigure(0, weight=1, uniform="col")
        container.grid_columnconfigure(1, weight=1, uniform="col")
        container.grid_rowconfigure(1, weight=3, uniform="row")
        container.grid_rowconfigure(2, weight=2, uniform="row")

        # ───────── Barra de botones (fila 0) ─────────
        botones = [
            ("▶️ Analizar",           "#00b894", self.analizar_codigo),
            ("📂 Cargar .txt",        "#0984e3", self.cargar_archivo),
            ("💾 Guardar resultado",  "#fdcb6e", self.guardar_resultado),
            ("🧹 Limpiar todo",       "#d63031", self.limpiar),
            ("🌳 Ver árbol completo", "#6c5ce7", self.abrir_arbol_ampliado),
            ("📊 Ver Tablas",         "#e17055", self.mostrar_tablas),
        ]
        btn_frame = tk.Frame(container, bg="#1e1e1e")
        btn_frame.grid(row=0, column=0, columnspan=2, pady=(20,10))
        for txt, col, cmd in botones:
            b = tk.Button(btn_frame, text=txt, command=cmd,
                          font=("Segoe UI",12), bg=col, fg="white",
                          bd=0, relief="flat", padx=10, pady=5)
            b.pack(side="left", padx=5)
            b.bind("<Enter>", lambda e,c=col: e.widget.config(bg="white", fg="#1e1e1e"))
            b.bind("<Leave>", lambda e,c=col: e.widget.config(bg=c, fg="white"))

        # ───────── Panel de entrada (fila 1–2, col 0) ─────────
        frame_in = tk.LabelFrame(container, text="📝 Código de entrada",
                                 fg="white", bg="#1e1e1e",
                                 font=("Segoe UI",12,"bold"),
                                 bd=0, relief="flat")
        frame_in.grid(row=1, column=0, rowspan=2, sticky="nsew",
                      padx=20, pady=20)
        self.texto_entrada = tk.Text(frame_in, font=("Fira Code",12),
                                     bg="#2d2d2d", fg="white",
                                     insertbackground="white",
                                     bd=0, relief="flat")
        self.texto_entrada.pack(fill="both", expand=True, padx=5, pady=5)
        self.texto_entrada.bind("<KeyRelease>", self._expandir_textarea)

        # ───────── Resultado (fila 1, col 1) ─────────
        frame_res = tk.LabelFrame(container, text="📋 Resultado del análisis",
                                  fg="white", bg="#1e1e1e",
                                  font=("Segoe UI",12,"bold"),
                                  bd=0, relief="flat")
        frame_res.grid(row=1, column=1, sticky="nsew",
                       padx=(10,20), pady=(20,5))
        self.resultado_texto = tk.Text(frame_res, font=("Fira Code",12),
                                       bg="#2d2d2d", fg="white",
                                       insertbackground="white",
                                       bd=0, relief="flat")
        self.resultado_texto.pack(fill="both", expand=True, padx=5, pady=5)
        self.resultado_texto.bind("<KeyRelease>", self._expandir_resultado)

        # ───────── Consola (fila 2, col 1) ─────────
        frame_con = tk.LabelFrame(container, text="🧪 Consola de ejecución",
                                  fg="white", bg="#1e1e1e",
                                  font=("Segoe UI",12,"bold"),
                                  bd=0, relief="flat")
        frame_con.grid(row=2, column=1, sticky="nsew",
                       padx=(10,20), pady=(5,20))
        self.consola = tk.Text(frame_con, font=("Fira Code",11),
                               bg="#2d2d2d", fg="#00ff00",
                               insertbackground="#00ff00",
                               bd=0, relief="flat")
        self.consola.pack(fill="both", expand=True, padx=5, pady=5)

        # ───────── Imagen del árbol ─────────
        self.imagen_arbol = tk.Label(frame_res, bg="#1e1e1e")
        self.imagen_arbol.pack(pady=5)

        # Inicializar datos para las tablas
        self.tokens   = []
        self.sint_err = []
        self.sem_err  = []
        self.ruta_imagen = None

    # ─ Métodos auxiliares ────────────────────────────────────────────────
    def _expandir_textarea(self, e=None):
        lines = int(self.texto_entrada.index('end-1c').split('.')[0])
        self.texto_entrada.config(height=min(max(lines,1),20))

    def _expandir_resultado(self, e=None):
        lines = int(self.resultado_texto.index('end-1c').split('.')[0])
        self.resultado_texto.config(height=min(max(lines,1),25))

    def _redibujar_fondo(self, evt):
        if not os.path.exists(self.bg_path):
            return
        img = Image.open(self.bg_path).convert("RGBA")
        img = img.resize((evt.width, evt.height))
        img = img.filter(ImageFilter.GaussianBlur(4))
        alpha = Image.new('L', img.size, 100)
        img.putalpha(alpha)
        self._bg = ImageTk.PhotoImage(img)
        self.canvas.delete("bg")
        self.canvas.create_image(0,0,anchor="nw",image=self._bg, tags="bg")

    # ─ Análisis completo ────────────────────────────────────────────────
    def analizar_codigo(self):
        codigo = self.texto_entrada.get("1.0", tk.END).strip()
        if not codigo:
            return messagebox.showwarning("Advertencia", "Ingresa código.")

        # Léxico
        self.tokens, self.lex_err = analizar_lexico(codigo)

        # Sintáctico y semántico
        lang = detectar_lenguaje(codigo)
        self.sint_err = []
        self.sem_err  = []
        if not self.lex_err:
            self.sint_err = analizar_sintactico_antlr(codigo, lang)
        if lang == "Python" and not self.lex_err:
            self.sem_err = analizar_semantico(codigo)

        # Construir resultado de texto
        txt  = f"Lenguaje: {lang}\n\nTokens:\n"
        txt += "".join(f"  [{t}]→{v}\n" for t,v in self.tokens)
        txt += "\n\nErrores Léxicos:\n"
        txt += ("\n".join(f"⚠️ {e}" for e in self.lex_err) if self.lex_err else "✅ Ninguno")
        txt += "\n\nErrores Sintácticos:\n"
        txt += ("\n".join(f"❌ {e}" for e in self.sint_err) if self.sint_err else "✅ Ninguno")
        txt += "\n\nErrores Semánticos:\n"
        txt += ("\n".join(f"⚠️ {e}" for e in self.sem_err) if self.sem_err else "✅ Ninguno")

        self.resultado_texto.delete("1.0", tk.END)
        self.resultado_texto.insert(tk.END, txt)

        # ─── Intentar generar el árbol ────────────────────────────────
        try:
            self.ruta_imagen = generar_arbol(codigo)
            img = Image.open(self.ruta_imagen).resize((600,300))
            self._imgtk = ImageTk.PhotoImage(img)
            self.imagen_arbol.config(image=self._imgtk)
        except SyntaxError as err:
            # capturamos el error de Graphviz como sintáctico
            self.sint_err.append(str(err))
            self.imagen_arbol.config(image="")
            self.ruta_imagen = None

        # Simulación de consola
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

        # Generar y mostrar árbol
        self.ruta_imagen = generar_arbol(codigo)
        img = Image.open(self.ruta_imagen).resize((600,300))
        self._imgtk = ImageTk.PhotoImage(img)
        self.imagen_arbol.config(image=self._imgtk)

        # Simulación de consola (igual que antes)
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
        win.configure(bg="#1e1e1e")
        win.geometry("1000x600")

        frm = tk.Frame(win, bg="#1e1e1e")
        frm.pack(fill="both", expand=True, padx=10, pady=10)
        frm.grid_columnconfigure(0, weight=1)
        frm.grid_columnconfigure(1, weight=1)
        frm.grid_rowconfigure(0, weight=1)
        frm.grid_rowconfigure(1, weight=1)

        def crear_frame(r, c, title):
            lf = tk.LabelFrame(frm, text=title, fg="white", bg="#1e1e1e",
                               font=("Segoe UI",11,"bold"), bd=0, relief="flat")
            lf.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
            return lf

        # 1) Tokens (0,0)
        lf1 = crear_frame(0, 0, "🪙 Tokens")
        tv1 = ttk.Treeview(lf1, columns=("Tipo","Valor"), show="headings")
        tv1.heading("Tipo",  text="Tipo");  tv1.heading("Valor", text="Valor")
        for t,v in self.tokens:
            tv1.insert("", "end", values=(t, v))
        tv1.pack(fill="both", expand=True)

        # 2) Errores Léxicos (0,1)
        lf2 = crear_frame(0, 1, "⚠️ Errores Léxicos")
        tv2 = ttk.Treeview(lf2, columns=("Índice","Mensaje"), show="headings")
        tv2.heading("Índice",  text="#");      tv2.heading("Mensaje", text="Mensaje")
        for i, err in enumerate(self.lex_err, 1):
            tv2.insert("", "end", values=(i, err))
        tv2.pack(fill="both", expand=True)

        # 3) Errores Sintácticos (1,0)
        lf3 = crear_frame(1, 0, "❌ Errores Sintácticos")
        tv3 = ttk.Treeview(lf3, columns=("Ubicación","Mensaje"), show="headings")
        tv3.heading("Ubicación", text="Línea:Col"); tv3.heading("Mensaje", text="Mensaje")
        for err in self.sint_err:
            if " " in err:
                loc, msg = err.split("  ",1)
            else:
                loc, msg = "-", err
            tv3.insert("", "end", values=(loc, msg))
        tv3.pack(fill="both", expand=True)

        # 4) Errores Semánticos (1,1)
        lf4 = crear_frame(1, 1, "⚠️ Errores Semánticos")
        tv4 = ttk.Treeview(lf4, columns=("Índice","Mensaje"), show="headings")
        tv4.heading("Índice", text="#"); tv4.heading("Mensaje", text="Mensaje")
        for i, msg in enumerate(self.sem_err, 1):
            tv4.insert("", "end", values=(i, msg))
        tv4.pack(fill="both", expand=True)

    # ─ Mostrar árbol en nueva ventana ──────────────────────────────────
    def abrir_arbol_ampliado(self):
        if not self.ruta_imagen:
            return messagebox.showinfo("Info","Genera primero el árbol.")
        top = Toplevel(self.root)
        img = Image.open(self.ruta_imagen)
        w,h = img.size
        top.geometry(f"{w+20}x{h+20}")
        cnv = tk.Canvas(top, width=w, height=h, bg="#1e1e1e")
        cnv.pack()
        imgtk = ImageTk.PhotoImage(img)
        cnv.create_image(0,0,anchor="nw", image=imgtk)
        cnv.image = imgtk

    # ─ Cargar archivo ────────────────────────────────────────────────
    def cargar_archivo(self):
        path = filedialog.askopenfilename(filetypes=[("TXT","*.txt")])
        if path:
            self.texto_entrada.delete("1.0", tk.END)
            self.texto_entrada.insert(tk.END, open(path, encoding="utf-8").read())

    # ─ Guardar resultado ────────────────────────────────────────────
    def guardar_resultado(self):
        contenido = self.resultado_texto.get("1.0", tk.END).strip()
        if not contenido:
            return messagebox.showwarning("Advertencia", "No hay resultados que guardar.")
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Archivo de texto","*.txt")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(contenido)

    # ─ Limpiar todos los campos ─────────────────────────────────────
    def limpiar(self):
        self.texto_entrada.delete("1.0", tk.END)
        self.resultado_texto.delete("1.0", tk.END)
        self.consola.delete("1.0", tk.END)
        self.imagen_arbol.config(image="")
        self.ruta_imagen = None


# ─ Arrancar la app ─────────────────────────────────────────
if __name__ == "__main__":
    root=tk.Tk()
    SimuladorCompiladorApp(root)
    root.mainloop()
