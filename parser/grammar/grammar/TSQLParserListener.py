# Generated from grammar/TSQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TSQLParserParser import TSQLParserParser
else:
    from TSQLParserParser import TSQLParserParser

# This class defines a complete listener for a parse tree produced by TSQLParserParser.
class TSQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by TSQLParserParser#sql_script.
    def enterSql_script(self, ctx:TSQLParserParser.Sql_scriptContext):
        pass

    # Exit a parse tree produced by TSQLParserParser#sql_script.
    def exitSql_script(self, ctx:TSQLParserParser.Sql_scriptContext):
        pass


    # Enter a parse tree produced by TSQLParserParser#sql_stmt.
    def enterSql_stmt(self, ctx:TSQLParserParser.Sql_stmtContext):
        pass

    # Exit a parse tree produced by TSQLParserParser#sql_stmt.
    def exitSql_stmt(self, ctx:TSQLParserParser.Sql_stmtContext):
        pass


    # Enter a parse tree produced by TSQLParserParser#create_table.
    def enterCreate_table(self, ctx:TSQLParserParser.Create_tableContext):
        pass

    # Exit a parse tree produced by TSQLParserParser#create_table.
    def exitCreate_table(self, ctx:TSQLParserParser.Create_tableContext):
        pass


    # Enter a parse tree produced by TSQLParserParser#column_def.
    def enterColumn_def(self, ctx:TSQLParserParser.Column_defContext):
        pass

    # Exit a parse tree produced by TSQLParserParser#column_def.
    def exitColumn_def(self, ctx:TSQLParserParser.Column_defContext):
        pass


    # Enter a parse tree produced by TSQLParserParser#type_name.
    def enterType_name(self, ctx:TSQLParserParser.Type_nameContext):
        pass

    # Exit a parse tree produced by TSQLParserParser#type_name.
    def exitType_name(self, ctx:TSQLParserParser.Type_nameContext):
        pass



del TSQLParserParser