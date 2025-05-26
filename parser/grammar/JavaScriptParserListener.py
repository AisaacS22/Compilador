# Generated from grammar/JavaScriptParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JavaScriptParserParser import JavaScriptParserParser
else:
    from JavaScriptParserParser import JavaScriptParserParser

# This class defines a complete listener for a parse tree produced by JavaScriptParserParser.
class JavaScriptParserListener(ParseTreeListener):

    # Enter a parse tree produced by JavaScriptParserParser#program.
    def enterProgram(self, ctx:JavaScriptParserParser.ProgramContext):
        pass

    # Exit a parse tree produced by JavaScriptParserParser#program.
    def exitProgram(self, ctx:JavaScriptParserParser.ProgramContext):
        pass


    # Enter a parse tree produced by JavaScriptParserParser#statement.
    def enterStatement(self, ctx:JavaScriptParserParser.StatementContext):
        pass

    # Exit a parse tree produced by JavaScriptParserParser#statement.
    def exitStatement(self, ctx:JavaScriptParserParser.StatementContext):
        pass


    # Enter a parse tree produced by JavaScriptParserParser#assignment.
    def enterAssignment(self, ctx:JavaScriptParserParser.AssignmentContext):
        pass

    # Exit a parse tree produced by JavaScriptParserParser#assignment.
    def exitAssignment(self, ctx:JavaScriptParserParser.AssignmentContext):
        pass


    # Enter a parse tree produced by JavaScriptParserParser#expr.
    def enterExpr(self, ctx:JavaScriptParserParser.ExprContext):
        pass

    # Exit a parse tree produced by JavaScriptParserParser#expr.
    def exitExpr(self, ctx:JavaScriptParserParser.ExprContext):
        pass



del JavaScriptParserParser