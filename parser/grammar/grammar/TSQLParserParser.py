# Generated from grammar/TSQLParser.g4 by ANTLR 4.13.2
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
        4,1,9,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        28,8,2,10,2,12,2,31,9,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,
        2,4,6,8,0,1,1,0,6,7,36,0,13,1,0,0,0,2,18,1,0,0,0,4,20,1,0,0,0,6,
        34,1,0,0,0,8,37,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,
        0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,
        5,0,0,1,17,1,1,0,0,0,18,19,3,4,2,0,19,3,1,0,0,0,20,21,5,1,0,0,21,
        22,5,2,0,0,22,23,5,8,0,0,23,24,5,3,0,0,24,29,3,6,3,0,25,26,5,4,0,
        0,26,28,3,6,3,0,27,25,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,
        1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,5,0,0,33,5,1,0,0,0,34,
        35,5,8,0,0,35,36,3,8,4,0,36,7,1,0,0,0,37,38,7,0,0,0,38,9,1,0,0,0,
        2,13,29
    ]

class TSQLParserParser ( Parser ):

    grammarFileName = "TSQLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'TABLE'", "'('", "','", "')'", 
                     "'INT'", "'VARCHAR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "WS" ]

    RULE_sql_script = 0
    RULE_sql_stmt = 1
    RULE_create_table = 2
    RULE_column_def = 3
    RULE_type_name = 4

    ruleNames =  [ "sql_script", "sql_stmt", "create_table", "column_def", 
                   "type_name" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Sql_scriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TSQLParserParser.EOF, 0)

        def sql_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TSQLParserParser.Sql_stmtContext)
            else:
                return self.getTypedRuleContext(TSQLParserParser.Sql_stmtContext,i)


        def getRuleIndex(self):
            return TSQLParserParser.RULE_sql_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_script" ):
                listener.enterSql_script(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_script" ):
                listener.exitSql_script(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql_script" ):
                return visitor.visitSql_script(self)
            else:
                return visitor.visitChildren(self)




    def sql_script(self):

        localctx = TSQLParserParser.Sql_scriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sql_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 10
                self.sql_stmt()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(TSQLParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sql_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_table(self):
            return self.getTypedRuleContext(TSQLParserParser.Create_tableContext,0)


        def getRuleIndex(self):
            return TSQLParserParser.RULE_sql_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_stmt" ):
                listener.enterSql_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_stmt" ):
                listener.exitSql_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql_stmt" ):
                return visitor.visitSql_stmt(self)
            else:
                return visitor.visitChildren(self)




    def sql_stmt(self):

        localctx = TSQLParserParser.Sql_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sql_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.create_table()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Create_tableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TSQLParserParser.ID, 0)

        def column_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TSQLParserParser.Column_defContext)
            else:
                return self.getTypedRuleContext(TSQLParserParser.Column_defContext,i)


        def getRuleIndex(self):
            return TSQLParserParser.RULE_create_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_table" ):
                listener.enterCreate_table(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_table" ):
                listener.exitCreate_table(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate_table" ):
                return visitor.visitCreate_table(self)
            else:
                return visitor.visitChildren(self)




    def create_table(self):

        localctx = TSQLParserParser.Create_tableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(TSQLParserParser.T__0)
            self.state = 21
            self.match(TSQLParserParser.T__1)
            self.state = 22
            self.match(TSQLParserParser.ID)
            self.state = 23
            self.match(TSQLParserParser.T__2)
            self.state = 24
            self.column_def()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 25
                self.match(TSQLParserParser.T__3)
                self.state = 26
                self.column_def()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(TSQLParserParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TSQLParserParser.ID, 0)

        def type_name(self):
            return self.getTypedRuleContext(TSQLParserParser.Type_nameContext,0)


        def getRuleIndex(self):
            return TSQLParserParser.RULE_column_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_def" ):
                listener.enterColumn_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_def" ):
                listener.exitColumn_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_def" ):
                return visitor.visitColumn_def(self)
            else:
                return visitor.visitChildren(self)




    def column_def(self):

        localctx = TSQLParserParser.Column_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_column_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(TSQLParserParser.ID)
            self.state = 35
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSQLParserParser.RULE_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_name" ):
                listener.enterType_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_name" ):
                listener.exitType_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = TSQLParserParser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
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





