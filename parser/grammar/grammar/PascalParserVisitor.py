# Generated from grammar/PascalParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PascalParserParser import PascalParserParser
else:
    from PascalParserParser import PascalParserParser

# This class defines a complete generic visitor for a parse tree produced by PascalParserParser.

class PascalParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PascalParserParser#programa.
    def visitPrograma(self, ctx:PascalParserParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParserParser#bloque.
    def visitBloque(self, ctx:PascalParserParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParserParser#instruccion.
    def visitInstruccion(self, ctx:PascalParserParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParserParser#asignacion.
    def visitAsignacion(self, ctx:PascalParserParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParserParser#llamada.
    def visitLlamada(self, ctx:PascalParserParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParserParser#expr.
    def visitExpr(self, ctx:PascalParserParser.ExprContext):
        return self.visitChildren(ctx)



del PascalParserParser