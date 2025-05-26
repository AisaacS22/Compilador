
import re

def analizar_semantico(codigo, lenguaje):
    errores = []
    declaradas = set()
    lineas = codigo.strip().splitlines()

    for i, linea in enumerate(lineas, start=1):
        stripped = linea.strip()

        if lenguaje == "Python":
            match_asignacion = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$', stripped)
            if match_asignacion:
                declaradas.add(match_asignacion.group(1))
                continue
            match_print = re.match(r'^print\s*\((.*)\)$', stripped)
            if match_print:
                variables = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', match_print.group(1))
                for var in variables:
                    if var not in declaradas and var not in ['print']:
                        errores.append(f"Línea {i}: Variable no declarada → \"{var}\"")

        elif lenguaje == "T-SQL":
            match_declare = re.match(r'^DECLARE\s+@([a-zA-Z_][a-zA-Z0-9_]*)\s+', stripped, re.IGNORECASE)
            if match_declare:
                declaradas.add(match_declare.group(1).lower())
                continue
            variables = re.findall(r'@([a-zA-Z_][a-zA-Z0-9_]*)', stripped)
            for var in variables:
                if var.lower() not in declaradas:
                    errores.append(f"Línea {i}: Variable @{var} no declarada")

        elif lenguaje == "Pascal":
            match_var = re.match(r'^var\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*:', stripped, re.IGNORECASE)
            if match_var:
                var_name = match_var.group(1)
                if var_name in declaradas:
                    errores.append(f"Línea {i}: Variable duplicada → {var_name}")
                else:
                    declaradas.add(var_name)
                continue
            usadas = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', stripped)
            for var in usadas:
                if var not in declaradas and var.lower() not in ['begin', 'end', 'writeln', 'readln', 'program', 'if', 'then', 'else', 'for', 'to', 'do']:
                    errores.append(f"Línea {i}: Variable no declarada → {var}")

        elif lenguaje == "JavaScript":
            match_declaracion = re.match(r'^(let|var|const)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=.*;$', stripped)
            if match_declaracion:
                declaradas.add(match_declaracion.group(2))
                continue
            usadas = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', stripped)
            for var in usadas:
                if var not in declaradas and var not in ['console', 'log', 'function', 'if', 'else', 'for', 'return']:
                    errores.append(f"Línea {i}: Variable no declarada → {var}")

        elif lenguaje == "C++":
            match_var = re.match(r'^(int|float|string|char|double)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=.*;$', stripped)
            if match_var:
                declaradas.add(match_var.group(2))
                continue
            usadas = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', stripped)
            for var in usadas:
                if var not in declaradas and var not in ['int', 'return', 'main', 'std', 'cout', 'cin', 'include']:
                    errores.append(f"Línea {i}: Variable no declarada → {var}")

        elif lenguaje == "PL/SQL":
            match_var = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s+\w+;$', stripped)
            if match_var:
                var_name = match_var.group(1)
                declaradas.add(var_name)
                continue
            usadas = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', stripped)
            for var in usadas:
                if var not in declaradas and var not in ['BEGIN', 'END', 'EXCEPTION', 'WHEN', 'THEN', 'RAISE_APPLICATION_ERROR', 'DBMS_OUTPUT']:
                    errores.append(f"Línea {i}: Variable no declarada → {var}")

        elif lenguaje == "HTML":
            pass  # Semántica HTML normalmente requiere un DOM real, se omite en esta fase.

    return errores
