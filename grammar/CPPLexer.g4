lexer grammar CPPLexer;

INCLUDE: '#include';
COUT: 'cout';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;