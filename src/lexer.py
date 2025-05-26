import re

# Diccionario extendido de clasificaciones por categoría más específica
PALABRAS_CLASIFICADAS = {
    "PALABRA_RESERVADA": {
        "Python": {"def", "return", "if", "else", "while", "for", "print", "import", "class"},
        "T-SQL": {"SELECT", "FROM", "WHERE", "INSERT", "UPDATE", "DELETE", "CREATE", "TABLE"},
        "C++": {"int", "float", "char", "double", "void", "main", "cout", "cin"},
        "JavaScript": {"function", "let", "const", "var", "if", "else"},
        "Pascal": {"program", "begin", "end", "writeln", "var"},
        "PL/SQL": {"DECLARE", "BEGIN", "END", "DBMS_OUTPUT", "EXCEPTION"},
        "HTML": {"html", "head", "title", "body", "p", "h1", "h2", "div"}
    },
    "FUNCION": {"print", "console.log", "DBMS_OUTPUT.PUT_LINE", "writeln", "cout"},
    "CICLO": {"for", "while", "do"},
    "CONDICIONAL": {"if", "else"},
    "CRUD": {"SELECT", "INSERT", "UPDATE", "DELETE"},
    "CLASE": {"class"},
    "VARIABLE": set(),  # Será poblado dinámicamente si lo deseas
    "CONSTANTE": set(),  # Números o cadenas
}

# Expresiones regulares para reconocimiento
patron_tokens = [
    ('NUMERO', r'\b\d+(\.\d+)?\b'),
    ('CADENA', r'"[^"\n]*"|\'[^\'\n]*\''),
    ('IDENTIFICADOR', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('ETIQUETA_HTML', r'</?[a-zA-Z][a-zA-Z0-9]*>'),
    ('OPERADOR', r'==|!=|<=|>=|:=|=|\+|\-|\*|\/|<|>|\|\||&&|!'),
    ('PUNTUACION', r'[;:{}()\[\],.]'),
    ('COMENTARIO_LINEA', r'//.*|--.*'),
]

def analizar_lexico(codigo, lenguaje="General"):
    tokens = []
    errores = []

    lineas = codigo.strip().splitlines()
    for num_linea, linea in enumerate(lineas, start=1):
        index = 0
        while index < len(linea):
            match = None
            for tipo, patron in patron_tokens:
                regex = re.compile(patron)
                match = regex.match(linea, index)
                if match:
                    valor = match.group()
                    tipo_final = tipo

                    if tipo == 'IDENTIFICADOR':
                        valor_mayus = valor.upper()
                        encontrado = False

                        # Detectar por lenguaje actual
                        if lenguaje in PALABRAS_CLASIFICADAS["PALABRA_RESERVADA"]:
                            if valor in PALABRAS_CLASIFICADAS["PALABRA_RESERVADA"][lenguaje]:
                                tipo_final = 'PALABRA_RESERVADA'
                                encontrado = True

                        # Clasificación extendida global
                        if not encontrado:
                            for clase, palabras in PALABRAS_CLASIFICADAS.items():
                                if clase != "PALABRA_RESERVADA" and valor in palabras:
                                    tipo_final = clase
                                    break

                    elif tipo == 'NUMERO':
                        tipo_final = 'CONSTANTE'
                    elif tipo == 'CADENA':
                        tipo_final = 'CONSTANTE'

                    tokens.append((tipo_final, valor))
                    index = match.end()
                    break

            if not match:
                if linea[index].isspace():
                    index += 1
                else:
                    errores.append(f"Línea {num_linea}: Símbolo no reconocido → '{linea[index]}'")
                    index += 1

    return tokens, errores
