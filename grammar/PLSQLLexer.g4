lexer grammar PLSQLLexer;

BEGIN: 'BEGIN';
END: 'END';
INSERT: 'INSERT';
INTO: 'INTO';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;