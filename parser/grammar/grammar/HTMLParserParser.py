# Generated from grammar/HTMLParser.g4 by ANTLR 4.13.2
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
        4,1,6,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,4,3,4,32,8,4,1,4,0,0,5,0,2,4,6,8,0,0,30,0,13,1,0,0,0,2,
        18,1,0,0,0,4,22,1,0,0,0,6,26,1,0,0,0,8,31,1,0,0,0,10,12,3,2,1,0,
        11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,
        0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,3,4,2,0,19,
        20,3,8,4,0,20,21,3,6,3,0,21,3,1,0,0,0,22,23,5,1,0,0,23,24,5,4,0,
        0,24,25,5,2,0,0,25,5,1,0,0,0,26,27,5,3,0,0,27,28,5,4,0,0,28,29,5,
        2,0,0,29,7,1,0,0,0,30,32,5,5,0,0,31,30,1,0,0,0,31,32,1,0,0,0,32,
        9,1,0,0,0,2,13,31
    ]

class HTMLParserParser ( Parser ):

    grammarFileName = "HTMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'</'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "TEXT", "WS" ]

    RULE_document = 0
    RULE_element = 1
    RULE_open_tag = 2
    RULE_close_tag = 3
    RULE_content = 4

    ruleNames =  [ "document", "element", "open_tag", "close_tag", "content" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ID=4
    TEXT=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HTMLParserParser.EOF, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParserParser.ElementContext)
            else:
                return self.getTypedRuleContext(HTMLParserParser.ElementContext,i)


        def getRuleIndex(self):
            return HTMLParserParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = HTMLParserParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 10
                self.element()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(HTMLParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def open_tag(self):
            return self.getTypedRuleContext(HTMLParserParser.Open_tagContext,0)


        def content(self):
            return self.getTypedRuleContext(HTMLParserParser.ContentContext,0)


        def close_tag(self):
            return self.getTypedRuleContext(HTMLParserParser.Close_tagContext,0)


        def getRuleIndex(self):
            return HTMLParserParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = HTMLParserParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.open_tag()
            self.state = 19
            self.content()
            self.state = 20
            self.close_tag()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HTMLParserParser.ID, 0)

        def getRuleIndex(self):
            return HTMLParserParser.RULE_open_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpen_tag" ):
                listener.enterOpen_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpen_tag" ):
                listener.exitOpen_tag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpen_tag" ):
                return visitor.visitOpen_tag(self)
            else:
                return visitor.visitChildren(self)




    def open_tag(self):

        localctx = HTMLParserParser.Open_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_open_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(HTMLParserParser.T__0)
            self.state = 23
            self.match(HTMLParserParser.ID)
            self.state = 24
            self.match(HTMLParserParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Close_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HTMLParserParser.ID, 0)

        def getRuleIndex(self):
            return HTMLParserParser.RULE_close_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose_tag" ):
                listener.enterClose_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose_tag" ):
                listener.exitClose_tag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClose_tag" ):
                return visitor.visitClose_tag(self)
            else:
                return visitor.visitChildren(self)




    def close_tag(self):

        localctx = HTMLParserParser.Close_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_close_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(HTMLParserParser.T__2)
            self.state = 27
            self.match(HTMLParserParser.ID)
            self.state = 28
            self.match(HTMLParserParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(HTMLParserParser.TEXT, 0)

        def getRuleIndex(self):
            return HTMLParserParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = HTMLParserParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 30
                self.match(HTMLParserParser.TEXT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





