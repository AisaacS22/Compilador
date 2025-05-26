lexer grammar PythonLexer;

PRINT: 'print';
DEF: 'def';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;