grammar PythonParser;

file_input: (stmt)* EOF ;
stmt: simple_stmt ;
simple_stmt: expr_stmt ;
expr_stmt: ID '=' expr ;
expr: ID | NUMBER ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;