# src/lexer.py

import re
from tokens import PALABRAS_RESERVADAS

def eliminar_comentarios(codigo: str) -> str:
    """
    Elimina comentarios de línea (// …, # …) y de bloque (/* … */).
    """
    # Primero los comentarios de bloque (/* … */)
    bloque = re.compile(r'/\*.*?\*/', re.DOTALL)
    codigo = re.sub(bloque, '', codigo)
    # Luego comentarios de línea: // … y # …
    linea1 = re.compile(r'//.*?$' , re.MULTILINE)
    linea2 = re.compile(r'#.*?$'  , re.MULTILINE)
    codigo = re.sub(linea1, '', codigo)
    codigo = re.sub(linea2, '', codigo)
    return codigo

def analizar_lexico(texto: str):
    """
    Analiza el texto fuente, elimina comentarios, tokeniza y devuelve
    (tokens, errores_lexicos).
    """
    # 1) quitar comentarios
    codigo = eliminar_comentarios(texto)

    tokens = []
    errores = []

    # 2) patrones de token
    patron_tokens = [
        ('NUMERO',       r'\b\d+(\.\d+)?([eE][+-]?\d+)?\b'),
        ('IDENTIFICADOR',r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
        ('OPERADOR',     r'==|!=|<=|>=|\+\+|--|[+\-*/%=<>!&|^~]+'),
        ('PUNTUACION',   r'[;:{}()\[\],.]'),
        ('CADENA',       r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\''),
    ]

    index = 0
    longitud = len(codigo)
    while index < longitud:
        # saltar espacios
        if codigo[index].isspace():
            index += 1
            continue

        match = None
        for tipo, patron in patron_tokens:
            regex = re.compile(patron)
            match = regex.match(codigo, index)
            if match:
                valor = match.group()
                # detectar palabra reservada
                if tipo == 'IDENTIFICADOR':
                    for lang, keywords in PALABRAS_RESERVADAS.items():
                        if valor in keywords:
                            tipo = 'PALABRA_RESERVADA'
                            break
                tokens.append((tipo, valor))
                index = match.end()
                break

        # si no matcheó ningún token válido
        if not match:
            errores.append(f'Símbolo desconocido: {codigo[index]}')
            index += 1

    return tokens, errores
