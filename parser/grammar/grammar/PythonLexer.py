# Generated from grammar/PythonLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,40,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,5,2,24,8,2,10,2,12,2,27,9,
        2,1,3,3,3,30,8,3,1,3,1,3,1,4,4,4,35,8,4,11,4,12,4,36,1,4,1,4,0,0,
        5,1,1,3,2,5,3,7,4,9,5,1,0,3,3,0,65,90,95,95,97,122,4,0,48,57,65,
        90,95,95,97,122,2,0,9,9,32,32,42,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,17,1,0,0,0,5,21,1,0,0,
        0,7,29,1,0,0,0,9,34,1,0,0,0,11,12,5,112,0,0,12,13,5,114,0,0,13,14,
        5,105,0,0,14,15,5,110,0,0,15,16,5,116,0,0,16,2,1,0,0,0,17,18,5,100,
        0,0,18,19,5,101,0,0,19,20,5,102,0,0,20,4,1,0,0,0,21,25,7,0,0,0,22,
        24,7,1,0,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,
        0,26,6,1,0,0,0,27,25,1,0,0,0,28,30,5,13,0,0,29,28,1,0,0,0,29,30,
        1,0,0,0,30,31,1,0,0,0,31,32,5,10,0,0,32,8,1,0,0,0,33,35,7,2,0,0,
        34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,38,1,
        0,0,0,38,39,6,4,0,0,39,10,1,0,0,0,4,0,25,29,36,1,6,0,0
    ]

class PythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINT = 1
    DEF = 2
    IDENTIFIER = 3
    NEWLINE = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "'def'" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "DEF", "IDENTIFIER", "NEWLINE", "WS" ]

    ruleNames = [ "PRINT", "DEF", "IDENTIFIER", "NEWLINE", "WS" ]

    grammarFileName = "PythonLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


