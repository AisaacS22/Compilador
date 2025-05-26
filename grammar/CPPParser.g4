grammar CPPParser;

program: (statement)* EOF ;
statement: assignment ;
assignment: ID '=' expr ';' ;
expr: ID | NUMBER ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;