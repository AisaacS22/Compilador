# Generated from grammar/HTMLParser.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,39,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,5,3,23,8,3,10,3,12,3,26,9,3,1,
        4,4,4,29,8,4,11,4,12,4,30,1,5,4,5,34,8,5,11,5,12,5,35,1,5,1,5,0,
        0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,4,3,0,65,90,95,95,97,122,4,0,48,
        57,65,90,95,95,97,122,2,0,60,60,62,62,3,0,9,10,13,13,32,32,41,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,1,13,1,0,0,0,3,15,1,0,0,0,5,17,1,0,0,0,7,20,1,0,0,0,9,28,1,
        0,0,0,11,33,1,0,0,0,13,14,5,60,0,0,14,2,1,0,0,0,15,16,5,62,0,0,16,
        4,1,0,0,0,17,18,5,60,0,0,18,19,5,47,0,0,19,6,1,0,0,0,20,24,7,0,0,
        0,21,23,7,1,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,
        1,0,0,0,25,8,1,0,0,0,26,24,1,0,0,0,27,29,8,2,0,0,28,27,1,0,0,0,29,
        30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,10,1,0,0,0,32,34,7,3,0,
        0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,
        1,0,0,0,37,38,6,5,0,0,38,12,1,0,0,0,4,0,24,30,35,1,6,0,0
    ]

class HTMLParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    ID = 4
    TEXT = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'</'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "TEXT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "ID", "TEXT", "WS" ]

    grammarFileName = "HTMLParser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


