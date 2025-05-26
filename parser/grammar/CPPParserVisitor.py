# Generated from grammar/CPPParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CPPParserParser import CPPParserParser
else:
    from CPPParserParser import CPPParserParser

# This class defines a complete generic visitor for a parse tree produced by CPPParserParser.

class CPPParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CPPParserParser#program.
    def visitProgram(self, ctx:CPPParserParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParserParser#statement.
    def visitStatement(self, ctx:CPPParserParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParserParser#assignment.
    def visitAssignment(self, ctx:CPPParserParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParserParser#expr.
    def visitExpr(self, ctx:CPPParserParser.ExprContext):
        return self.visitChildren(ctx)



del CPPParserParser