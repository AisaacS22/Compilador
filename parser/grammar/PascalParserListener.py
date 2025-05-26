# Generated from grammar/PascalParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PascalParserParser import PascalParserParser
else:
    from PascalParserParser import PascalParserParser

# This class defines a complete listener for a parse tree produced by PascalParserParser.
class PascalParserListener(ParseTreeListener):

    # Enter a parse tree produced by PascalParserParser#programa.
    def enterPrograma(self, ctx:PascalParserParser.ProgramaContext):
        pass

    # Exit a parse tree produced by PascalParserParser#programa.
    def exitPrograma(self, ctx:PascalParserParser.ProgramaContext):
        pass


    # Enter a parse tree produced by PascalParserParser#bloque.
    def enterBloque(self, ctx:PascalParserParser.BloqueContext):
        pass

    # Exit a parse tree produced by PascalParserParser#bloque.
    def exitBloque(self, ctx:PascalParserParser.BloqueContext):
        pass


    # Enter a parse tree produced by PascalParserParser#instruccion.
    def enterInstruccion(self, ctx:PascalParserParser.InstruccionContext):
        pass

    # Exit a parse tree produced by PascalParserParser#instruccion.
    def exitInstruccion(self, ctx:PascalParserParser.InstruccionContext):
        pass


    # Enter a parse tree produced by PascalParserParser#asignacion.
    def enterAsignacion(self, ctx:PascalParserParser.AsignacionContext):
        pass

    # Exit a parse tree produced by PascalParserParser#asignacion.
    def exitAsignacion(self, ctx:PascalParserParser.AsignacionContext):
        pass


    # Enter a parse tree produced by PascalParserParser#llamada.
    def enterLlamada(self, ctx:PascalParserParser.LlamadaContext):
        pass

    # Exit a parse tree produced by PascalParserParser#llamada.
    def exitLlamada(self, ctx:PascalParserParser.LlamadaContext):
        pass


    # Enter a parse tree produced by PascalParserParser#expr.
    def enterExpr(self, ctx:PascalParserParser.ExprContext):
        pass

    # Exit a parse tree produced by PascalParserParser#expr.
    def exitExpr(self, ctx:PascalParserParser.ExprContext):
        pass



del PascalParserParser