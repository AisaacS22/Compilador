# Generated from grammar/PLSQLParser.g4 by ANTLR 4.13.2
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
        4,1,9,39,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,5,3,32,8,3,10,3,12,3,35,9,3,1,4,1,4,1,4,0,0,5,0,2,4,
        6,8,0,1,1,0,7,8,35,0,13,1,0,0,0,2,18,1,0,0,0,4,20,1,0,0,0,6,28,1,
        0,0,0,8,36,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,
        11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,
        1,17,1,1,0,0,0,18,19,3,4,2,0,19,3,1,0,0,0,20,21,5,1,0,0,21,22,5,
        2,0,0,22,23,5,7,0,0,23,24,5,3,0,0,24,25,5,4,0,0,25,26,3,6,3,0,26,
        27,5,5,0,0,27,5,1,0,0,0,28,33,3,8,4,0,29,30,5,6,0,0,30,32,3,8,4,
        0,31,29,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,7,1,
        0,0,0,35,33,1,0,0,0,36,37,7,0,0,0,37,9,1,0,0,0,2,13,33
    ]

class PLSQLParserParser ( Parser ):

    grammarFileName = "PLSQLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'INSERT'", "'INTO'", "'VALUES'", "'('", 
                     "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "WS" ]

    RULE_script = 0
    RULE_statement = 1
    RULE_insert_stmt = 2
    RULE_value_list = 3
    RULE_expr = 4

    ruleNames =  [ "script", "statement", "insert_stmt", "value_list", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    NUMBER=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PLSQLParserParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSQLParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLSQLParserParser.StatementContext,i)


        def getRuleIndex(self):
            return PLSQLParserParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = PLSQLParserParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(PLSQLParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def insert_stmt(self):
            return self.getTypedRuleContext(PLSQLParserParser.Insert_stmtContext,0)


        def getRuleIndex(self):
            return PLSQLParserParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PLSQLParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.insert_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Insert_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLSQLParserParser.ID, 0)

        def value_list(self):
            return self.getTypedRuleContext(PLSQLParserParser.Value_listContext,0)


        def getRuleIndex(self):
            return PLSQLParserParser.RULE_insert_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert_stmt" ):
                listener.enterInsert_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert_stmt" ):
                listener.exitInsert_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert_stmt" ):
                return visitor.visitInsert_stmt(self)
            else:
                return visitor.visitChildren(self)




    def insert_stmt(self):

        localctx = PLSQLParserParser.Insert_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_insert_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(PLSQLParserParser.T__0)
            self.state = 21
            self.match(PLSQLParserParser.T__1)
            self.state = 22
            self.match(PLSQLParserParser.ID)
            self.state = 23
            self.match(PLSQLParserParser.T__2)
            self.state = 24
            self.match(PLSQLParserParser.T__3)
            self.state = 25
            self.value_list()
            self.state = 26
            self.match(PLSQLParserParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLSQLParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(PLSQLParserParser.ExprContext,i)


        def getRuleIndex(self):
            return PLSQLParserParser.RULE_value_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_list" ):
                listener.enterValue_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_list" ):
                listener.exitValue_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_list" ):
                return visitor.visitValue_list(self)
            else:
                return visitor.visitChildren(self)




    def value_list(self):

        localctx = PLSQLParserParser.Value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.expr()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 29
                self.match(PLSQLParserParser.T__5)
                self.state = 30
                self.expr()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(PLSQLParserParser.ID, 0)

        def NUMBER(self):
            return self.getToken(PLSQLParserParser.NUMBER, 0)

        def getRuleIndex(self):
            return PLSQLParserParser.RULE_expr

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

        localctx = PLSQLParserParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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





