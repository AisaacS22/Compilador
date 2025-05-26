# Generated from grammar/JavaScriptParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JavaScriptParserParser import JavaScriptParserParser
else:
    from JavaScriptParserParser import JavaScriptParserParser

# This class defines a complete generic visitor for a parse tree produced by JavaScriptParserParser.

class JavaScriptParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JavaScriptParserParser#program.
    def visitProgram(self, ctx:JavaScriptParserParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParserParser#statement.
    def visitStatement(self, ctx:JavaScriptParserParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParserParser#assignment.
    def visitAssignment(self, ctx:JavaScriptParserParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParserParser#expr.
    def visitExpr(self, ctx:JavaScriptParserParser.ExprContext):
        return self.visitChildren(ctx)



del JavaScriptParserParser