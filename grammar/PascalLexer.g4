lexer grammar PascalLexer;

PROGRAM: 'program';
BEGIN: 'begin';
END: 'end';
WRITELN: 'writeln';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;