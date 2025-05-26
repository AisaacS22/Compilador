# Generated from grammar/PLSQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLSQLParserParser import PLSQLParserParser
else:
    from PLSQLParserParser import PLSQLParserParser

# This class defines a complete generic visitor for a parse tree produced by PLSQLParserParser.

class PLSQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLSQLParserParser#script.
    def visitScript(self, ctx:PLSQLParserParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSQLParserParser#statement.
    def visitStatement(self, ctx:PLSQLParserParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSQLParserParser#insert_stmt.
    def visitInsert_stmt(self, ctx:PLSQLParserParser.Insert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSQLParserParser#value_list.
    def visitValue_list(self, ctx:PLSQLParserParser.Value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLSQLParserParser#expr.
    def visitExpr(self, ctx:PLSQLParserParser.ExprContext):
        return self.visitChildren(ctx)



del PLSQLParserParser