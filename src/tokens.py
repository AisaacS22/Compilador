# tokens.py

PALABRAS_RESERVADAS = {
    "C++": [
        "int", "float", "double", "char", "if", "else", "return", "include",
        "using", "namespace", "cout", "cin", "main", "void"
    ],
    "HTML": [
        "html", "head", "body", "title", "div", "p", "a", "script", "meta", "link"
    ],
    "JavaScript": [
        "function", "return", "var", "let", "const", "if", "else", "console", "log", "document"
    ],
    "Pascal": [
        "begin", "end", "var", "program", "integer", "real", "if", "then", "writeln", "readln"
    ],
    "PL/SQL": [
        "DECLARE", "BEGIN", "END", "SELECT", "FROM", "CREATE", "TABLE",
        "INSERT", "UPDATE", "DELETE", "INTO", "VALUES"
    ],
    "Python": [
        "def", "print", "return", "if", "else", "import", "while", "for", "in", "range", "input"
    ],
    "T-SQL": [
        "CREATE", "TABLE", "SELECT", "INSERT", "UPDATE", "DELETE", "FROM", "WHERE", "INTO", "VALUES"
    ]
}

# Convertir todas a minúsculas para facilitar comparación en lexer
for lang in PALABRAS_RESERVADAS:
    PALABRAS_RESERVADAS[lang] = [pal.lower() for pal in PALABRAS_RESERVADAS[lang]]
