# Generated from grammar/PascalParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,54,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,
        1,1,1,1,2,1,2,3,2,32,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,
        43,8,4,10,4,12,4,46,9,4,3,4,48,8,4,1,4,1,4,1,5,1,5,1,5,0,0,6,0,2,
        4,6,8,10,0,1,1,0,10,12,51,0,12,1,0,0,0,2,18,1,0,0,0,4,31,1,0,0,0,
        6,33,1,0,0,0,8,37,1,0,0,0,10,51,1,0,0,0,12,13,5,1,0,0,13,14,5,10,
        0,0,14,15,5,2,0,0,15,16,3,2,1,0,16,17,5,3,0,0,17,1,1,0,0,0,18,24,
        5,4,0,0,19,20,3,4,2,0,20,21,5,2,0,0,21,23,1,0,0,0,22,19,1,0,0,0,
        23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,24,1,
        0,0,0,27,28,5,5,0,0,28,3,1,0,0,0,29,32,3,6,3,0,30,32,3,8,4,0,31,
        29,1,0,0,0,31,30,1,0,0,0,32,5,1,0,0,0,33,34,5,10,0,0,34,35,5,6,0,
        0,35,36,3,10,5,0,36,7,1,0,0,0,37,38,5,10,0,0,38,47,5,7,0,0,39,44,
        3,10,5,0,40,41,5,8,0,0,41,43,3,10,5,0,42,40,1,0,0,0,43,46,1,0,0,
        0,44,42,1,0,0,0,44,45,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,47,39,
        1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,9,0,0,50,9,1,0,0,0,51,
        52,7,0,0,0,52,11,1,0,0,0,4,24,31,44,47
    ]

class PascalParserParser ( Parser ):

    grammarFileName = "PascalParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'.'", "'begin'", 
                     "'end'", "':='", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "STRING", 
                      "WS" ]

    RULE_programa = 0
    RULE_bloque = 1
    RULE_instruccion = 2
    RULE_asignacion = 3
    RULE_llamada = 4
    RULE_expr = 5

    ruleNames =  [ "programa", "bloque", "instruccion", "asignacion", "llamada", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ID=10
    NUMBER=11
    STRING=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PascalParserParser.ID, 0)

        def bloque(self):
            return self.getTypedRuleContext(PascalParserParser.BloqueContext,0)


        def getRuleIndex(self):
            return PascalParserParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = PascalParserParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(PascalParserParser.T__0)
            self.state = 13
            self.match(PascalParserParser.ID)
            self.state = 14
            self.match(PascalParserParser.T__1)
            self.state = 15
            self.bloque()
            self.state = 16
            self.match(PascalParserParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParserParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(PascalParserParser.InstruccionContext,i)


        def getRuleIndex(self):
            return PascalParserParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = PascalParserParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(PascalParserParser.T__3)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 19
                self.instruccion()
                self.state = 20
                self.match(PascalParserParser.T__1)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(PascalParserParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(PascalParserParser.AsignacionContext,0)


        def llamada(self):
            return self.getTypedRuleContext(PascalParserParser.LlamadaContext,0)


        def getRuleIndex(self):
            return PascalParserParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = PascalParserParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.llamada()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PascalParserParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(PascalParserParser.ExprContext,0)


        def getRuleIndex(self):
            return PascalParserParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = PascalParserParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(PascalParserParser.ID)
            self.state = 34
            self.match(PascalParserParser.T__5)
            self.state = 35
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PascalParserParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(PascalParserParser.ExprContext,i)


        def getRuleIndex(self):
            return PascalParserParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)




    def llamada(self):

        localctx = PascalParserParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_llamada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(PascalParserParser.ID)
            self.state = 38
            self.match(PascalParserParser.T__6)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0):
                self.state = 39
                self.expr()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 40
                    self.match(PascalParserParser.T__7)
                    self.state = 41
                    self.expr()
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 49
            self.match(PascalParserParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PascalParserParser.ID, 0)

        def NUMBER(self):
            return self.getToken(PascalParserParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(PascalParserParser.STRING, 0)

        def getRuleIndex(self):
            return PascalParserParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = PascalParserParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





