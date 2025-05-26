grammar PLSQLParser;

script: (statement)* EOF ;
statement: insert_stmt ;
insert_stmt: 'INSERT' 'INTO' ID 'VALUES' '(' value_list ')' ;
value_list: expr (',' expr)* ;
expr: ID | NUMBER ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;