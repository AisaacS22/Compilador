# Generated from grammar/CPPParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CPPParserParser import CPPParserParser
else:
    from CPPParserParser import CPPParserParser

# This class defines a complete listener for a parse tree produced by CPPParserParser.
class CPPParserListener(ParseTreeListener):

    # Enter a parse tree produced by CPPParserParser#program.
    def enterProgram(self, ctx:CPPParserParser.ProgramContext):
        pass

    # Exit a parse tree produced by CPPParserParser#program.
    def exitProgram(self, ctx:CPPParserParser.ProgramContext):
        pass


    # Enter a parse tree produced by CPPParserParser#statement.
    def enterStatement(self, ctx:CPPParserParser.StatementContext):
        pass

    # Exit a parse tree produced by CPPParserParser#statement.
    def exitStatement(self, ctx:CPPParserParser.StatementContext):
        pass


    # Enter a parse tree produced by CPPParserParser#assignment.
    def enterAssignment(self, ctx:CPPParserParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CPPParserParser#assignment.
    def exitAssignment(self, ctx:CPPParserParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CPPParserParser#expr.
    def enterExpr(self, ctx:CPPParserParser.ExprContext):
        pass

    # Exit a parse tree produced by CPPParserParser#expr.
    def exitExpr(self, ctx:CPPParserParser.ExprContext):
        pass



del CPPParserParser