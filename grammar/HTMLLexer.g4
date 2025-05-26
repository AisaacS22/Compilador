lexer grammar HTMLLexer;

HTML: '<html>'; 
P: '<p>' | '</p>';
HEAD: '<head>' | '</head>';
TITLE: '<title>' | '</title>';
WS: [ \t\r\n]+ -> skip;