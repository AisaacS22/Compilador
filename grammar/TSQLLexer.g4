lexer grammar TSQLLexer;

CREATE: 'CREATE';
TABLE: 'TABLE';
SELECT: 'SELECT';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;