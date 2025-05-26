grammar HTMLParser;

document: (element)* EOF ;
element: open_tag content close_tag ;
open_tag: '<' ID '>' ;
close_tag: '</' ID '>' ;
content: TEXT? ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
TEXT: ~[<>]+ ;
WS: [ \t\r\n]+ -> skip ;