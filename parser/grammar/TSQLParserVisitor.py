# Generated from grammar/TSQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TSQLParserParser import TSQLParserParser
else:
    from TSQLParserParser import TSQLParserParser

# This class defines a complete generic visitor for a parse tree produced by TSQLParserParser.

class TSQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TSQLParserParser#sql_script.
    def visitSql_script(self, ctx:TSQLParserParser.Sql_scriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSQLParserParser#sql_stmt.
    def visitSql_stmt(self, ctx:TSQLParserParser.Sql_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSQLParserParser#create_table.
    def visitCreate_table(self, ctx:TSQLParserParser.Create_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSQLParserParser#column_def.
    def visitColumn_def(self, ctx:TSQLParserParser.Column_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSQLParserParser#type_name.
    def visitType_name(self, ctx:TSQLParserParser.Type_nameContext):
        return self.visitChildren(ctx)



del TSQLParserParser