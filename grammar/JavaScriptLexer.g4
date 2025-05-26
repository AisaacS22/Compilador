lexer grammar JavaScriptLexer;

FUNCTION: 'function';
CONSOLE: 'console.log';
VAR: 'var';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;