# ⚙️ SynthaCore – Simulador de Compilador

## Descripción
**SynthaCore** es una herramienta de simulación de compilador que permite:
- **Detectar** automáticamente el lenguaje fuente (C++, HTML, JavaScript, Pascal, PL/SQL, Python, T-SQL).  
- Realizar **análisis léxico**, **sintáctico** y **semántico**.  
- Visualizar **tokens**, **errores** y **árbol sintáctico** (Graphviz).  
- **Ejecutar** fragmentos sencillos (e.g. `print`, `CREATE TABLE`).  
- **Exportar** resultados y ver tablas de detalle.

---

## Estructura del Proyecto

simulador_compilador/
├─ parser/grammar/ # Grammars ANTLR4 → PythonLexer, PythonParser, etc.
├─ src/
│ ├─ main.py # GUI principal (Tkinter)
│ ├─ lexer.py # Análisis léxico (ahora con comentarios)
│ ├─ detector_lenguaje.py
│ ├─ semantic.py
│ ├─ tree_builder.py
│ └─ … otros módulos …
└─ trees/ # Árboles sintácticos generados (.png)


---

## Requisitos

- Python ≥ 3.8  
- Pip:  
  pip install antlr4-python3-runtime graphviz pillow
  
## Uso
Clona el repositorio y entra en la carpeta:

git clone <tu-repo-url>
cd simulador_compilador

Uso
Clona el repositorio y entra en la carpeta:

git clone <tu-repo-url>
cd simulador_compilador
# CompiladorFinal
