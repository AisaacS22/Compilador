grammar TSQLParser;

sql_script: (sql_stmt)* EOF ;
sql_stmt: create_table ;
create_table: 'CREATE' 'TABLE' ID '(' column_def (',' column_def)* ')' ;
column_def: ID type_name ;
type_name: 'INT' | 'VARCHAR' ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\r\n]+ -> skip ;