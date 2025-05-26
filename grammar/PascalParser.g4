grammar PascalParser;

programa: 'program' ID ';' bloque '.' ;
bloque: 'begin' (instruccion ';')* 'end' ;
instruccion: asignacion | llamada ;
asignacion: ID ':=' expr ;
llamada: ID '(' (expr (',' expr)*)? ')' ;
expr: ID | NUMBER | STRING ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER: [0-9]+ ;
STRING: '\'' .*? '\'' ;
WS: [ \t\r\n]+ -> skip ;