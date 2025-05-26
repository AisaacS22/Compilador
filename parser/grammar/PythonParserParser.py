# Generated from grammar/PythonParser.g4 by ANTLR 4.13.2
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
        4,1,4,29,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,0,0,5,0,2,4,6,8,0,1,1,0,2,3,24,0,13,1,0,0,0,2,18,1,0,0,0,4,20,
        1,0,0,0,6,22,1,0,0,0,8,26,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,
        15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,
        0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,3,4,2,0,19,3,1,0,0,0,20,21,3,
        6,3,0,21,5,1,0,0,0,22,23,5,2,0,0,23,24,5,1,0,0,24,25,3,8,4,0,25,
        7,1,0,0,0,26,27,7,0,0,0,27,9,1,0,0,0,1,13
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "NUMBER", "WS" ]

    RULE_file_input = 0
    RULE_stmt = 1
    RULE_simple_stmt = 2
    RULE_expr_stmt = 3
    RULE_expr = 4

    ruleNames =  [ "file_input", "stmt", "simple_stmt", "expr_stmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    NUMBER=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonParserParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StmtContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StmtContext,i)


        def getRuleIndex(self):
            return PythonParserParser.RULE_file_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_input" ):
                listener.enterFile_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_input" ):
                listener.exitFile_input(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_input" ):
                return visitor.visitFile_input(self)
            else:
                return visitor.visitChildren(self)




    def file_input(self):

        localctx = PythonParserParser.File_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 10
                self.stmt()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(PythonParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(PythonParserParser.Simple_stmtContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = PythonParserParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.simple_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_stmt(self):
            return self.getTypedRuleContext(PythonParserParser.Expr_stmtContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_simple_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stmt" ):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stmt" ):
                listener.exitSimple_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_stmt" ):
                return visitor.visitSimple_stmt(self)
            else:
                return visitor.visitChildren(self)




    def simple_stmt(self):

        localctx = PythonParserParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.expr_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonParserParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_expr_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_stmt" ):
                listener.enterExpr_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_stmt" ):
                listener.exitExpr_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_stmt" ):
                return visitor.visitExpr_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expr_stmt(self):

        localctx = PythonParserParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(PythonParserParser.ID)
            self.state = 23
            self.match(PythonParserParser.T__0)
            self.state = 24
            self.expr()
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
            return self.getToken(PythonParserParser.ID, 0)

        def NUMBER(self):
            return self.getToken(PythonParserParser.NUMBER, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_expr

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

        localctx = PythonParserParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
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





