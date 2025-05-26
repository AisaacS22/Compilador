import re

def detectar_lenguaje(texto):
    patrones = {
        "C++": [r"#include\s*<.*>", r"\bstd::", r"\bcout\b", r"\bcin\b", r"\busing\s+namespace\b"],
        "HTML": [r"<html>", r"</html>", r"<body>", r"<div>", r"<p>"],
        "JavaScript": [r"\bfunction\b", r"\bconsole\.log\b", r"\bvar\b", r"\blet\b", r"\bconst\b"],
        "Pascal": [r"\bprogram\b", r"\bbegin\b", r"\bend\b", r"\bwriteln\b", r"\bvar\b.*:.*;"],
        "PL/SQL": [r"\bDECLARE\b", r"\bBEGIN\b", r"\bEND\b", r"\bDBMS_OUTPUT\.PUT_LINE\b", r"\bEXCEPTION\b"],
        "Python": [r"\bdef\b", r"\bprint\s*\(", r"\bimport\b", r"\bself\b", r"\bclass\b"],
        "T-SQL": [r"\bSELECT\b\s+.*\s+FROM\b", r"\bINSERT\s+INTO\b", r"\bCREATE\s+TABLE\b", r"\bUPDATE\b", r"\bDELETE\b"]
    }

    puntajes = {lenguaje: 0 for lenguaje in patrones}

    for lenguaje, regex_list in patrones.items():
        for regex in regex_list:
            coincidencias = re.findall(regex, texto, re.IGNORECASE)
            puntajes[lenguaje] += len(coincidencias)

    lenguaje_detectado = max(puntajes, key=puntajes.get)
    return lenguaje_detectado if puntajes[lenguaje_detectado] > 0 else "Desconocido"
