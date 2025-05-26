# Generated from grammar/PLSQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLSQLParserParser import PLSQLParserParser
else:
    from PLSQLParserParser import PLSQLParserParser

# This class defines a complete listener for a parse tree produced by PLSQLParserParser.
class PLSQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by PLSQLParserParser#script.
    def enterScript(self, ctx:PLSQLParserParser.ScriptContext):
        pass

    # Exit a parse tree produced by PLSQLParserParser#script.
    def exitScript(self, ctx:PLSQLParserParser.ScriptContext):
        pass


    # Enter a parse tree produced by PLSQLParserParser#statement.
    def enterStatement(self, ctx:PLSQLParserParser.StatementContext):
        pass

    # Exit a parse tree produced by PLSQLParserParser#statement.
    def exitStatement(self, ctx:PLSQLParserParser.StatementContext):
        pass


    # Enter a parse tree produced by PLSQLParserParser#insert_stmt.
    def enterInsert_stmt(self, ctx:PLSQLParserParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by PLSQLParserParser#insert_stmt.
    def exitInsert_stmt(self, ctx:PLSQLParserParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by PLSQLParserParser#value_list.
    def enterValue_list(self, ctx:PLSQLParserParser.Value_listContext):
        pass

    # Exit a parse tree produced by PLSQLParserParser#value_list.
    def exitValue_list(self, ctx:PLSQLParserParser.Value_listContext):
        pass


    # Enter a parse tree produced by PLSQLParserParser#expr.
    def enterExpr(self, ctx:PLSQLParserParser.ExprContext):
        pass

    # Exit a parse tree produced by PLSQLParserParser#expr.
    def exitExpr(self, ctx:PLSQLParserParser.ExprContext):
        pass



del PLSQLParserParser