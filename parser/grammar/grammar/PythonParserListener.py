# Generated from grammar/PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParserParser import PythonParserParser
else:
    from PythonParserParser import PythonParserParser

# This class defines a complete listener for a parse tree produced by PythonParserParser.
class PythonParserListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParserParser#file_input.
    def enterFile_input(self, ctx:PythonParserParser.File_inputContext):
        pass

    # Exit a parse tree produced by PythonParserParser#file_input.
    def exitFile_input(self, ctx:PythonParserParser.File_inputContext):
        pass


    # Enter a parse tree produced by PythonParserParser#stmt.
    def enterStmt(self, ctx:PythonParserParser.StmtContext):
        pass

    # Exit a parse tree produced by PythonParserParser#stmt.
    def exitStmt(self, ctx:PythonParserParser.StmtContext):
        pass


    # Enter a parse tree produced by PythonParserParser#simple_stmt.
    def enterSimple_stmt(self, ctx:PythonParserParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by PythonParserParser#simple_stmt.
    def exitSimple_stmt(self, ctx:PythonParserParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by PythonParserParser#expr_stmt.
    def enterExpr_stmt(self, ctx:PythonParserParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by PythonParserParser#expr_stmt.
    def exitExpr_stmt(self, ctx:PythonParserParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by PythonParserParser#expr.
    def enterExpr(self, ctx:PythonParserParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParserParser#expr.
    def exitExpr(self, ctx:PythonParserParser.ExprContext):
        pass



del PythonParserParser