# Generated from grammar/PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParserParser import PythonParserParser
else:
    from PythonParserParser import PythonParserParser

# This class defines a complete generic visitor for a parse tree produced by PythonParserParser.

class PythonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParserParser#file_input.
    def visitFile_input(self, ctx:PythonParserParser.File_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParserParser#stmt.
    def visitStmt(self, ctx:PythonParserParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParserParser#simple_stmt.
    def visitSimple_stmt(self, ctx:PythonParserParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParserParser#expr_stmt.
    def visitExpr_stmt(self, ctx:PythonParserParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParserParser#expr.
    def visitExpr(self, ctx:PythonParserParser.ExprContext):
        return self.visitChildren(ctx)



del PythonParserParser