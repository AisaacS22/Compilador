# src/tree_builder.py

from graphviz import Digraph
import re, os, time

def _sanitize_label(texto):
    # Elimina corchetes, comillas y todo lo que Graphviz no tolere en IDs
    return re.sub(r'[^0-9A-Za-z_]', '_', texto)

def generar_arbol(codigo):
    """
    Intenta generar el árbol. Si falla, lanza una excepción controlada
    con el mensaje de Graphviz.
    """
    try:
        arbol = Digraph(format='png')
        arbol.attr('node', shape='box', style='filled',
                   color='#2d3436', fontname='Consolas',
                   fontcolor='white', fillcolor='#636e72')

        root_id = "Nodo_Raiz"
        arbol.node(root_id, "Programa")

        for i, linea in enumerate(codigo.strip().splitlines(), start=1):
            nid = f"linea_{i}"
            arbol.node(nid, f"Línea {i}")
            arbol.edge(root_id, nid)

            for j, token in enumerate(linea.strip().split(), start=1):
                label = _sanitize_label(token)
                tid   = f"{nid}_{j}"
                arbol.node(tid, token)  # mantiene label original
                arbol.edge(nid, tid)

        # Carpeta de salida
        if not os.path.exists("trees"):
            os.makedirs("trees")
        timestamp = int(time.time())
        salida = f"trees/arbol_{timestamp}"
        # Si falla aquí, capturamos abajo
        arbol.render(salida, cleanup=True)
        return salida + ".png"

    except Exception as e:
        # Propaga como SyntaxError para que main.py lo recoja
        raise SyntaxError(f"Graphviz error: {e}")
