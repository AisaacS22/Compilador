# src/tree_builder.py

import os
import time
import re
import html
from graphviz import Digraph

def _sanitize_id(nombre: str) -> str:
    """
    Devuelve un nombre válido para node IDs en Graphviz:
    sólo letras, números y guiones bajos.
    """
    return re.sub(r'[^0-9A-Za-z_]', '_', nombre)

def generar_arbol(codigo: str) -> str:
    """
    Genera un árbol sintáctico de las líneas y tokens de 'codigo'.
    - Cada línea es un subnodo de 'Programa'.
    - Cada token es un subnodo de su línea.
    Devuelve la ruta al PNG generado.
    Si Graphviz falla, lanza SyntaxError con el mensaje.
    """
    try:
        dot = Digraph(format='png')
        dot.attr(
            'node',
            shape='box',
            style='filled',
            color='#2d3436',
            fontname='Consolas',
            fontcolor='white',
            fillcolor='#636e72'
        )

        # Nodo raíz
        root_id = _sanitize_id("Nodo_Raiz")
        dot.node(root_id, "Programa")

        # Procesar cada línea
        for i, linea in enumerate(codigo.strip().splitlines(), start=1):
            line_id = _sanitize_id(f"linea_{i}")
            dot.node(line_id, f"Línea {i}")
            dot.edge(root_id, line_id)

            # Tokenizar: palabras (\w+) o cualquier carácter no espacio/no palabra
            tokens = re.findall(r'\w+|[^\s\w]', linea)
            for j, tok in enumerate(tokens, start=1):
                tid = _sanitize_id(f"{line_id}_{j}")
                label = html.escape(tok)  # escapa <, >, &, etc.
                dot.node(tid, label)
                dot.edge(line_id, tid)

        # Crear carpeta si no existe
        folder = "trees"
        os.makedirs(folder, exist_ok=True)

        # Guardar con timestamp único
        timestamp = int(time.time())
        path_no_ext = os.path.join(folder, f"arbol_{timestamp}")
        dot.render(path_no_ext, cleanup=True)

        return path_no_ext + ".png"

    except Exception as e:
        # Convierte cualquier error de Graphviz en SyntaxError
        raise SyntaxError(f"Graphviz error: {e}")
