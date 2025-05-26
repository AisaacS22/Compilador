# Generated from grammar/PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,30,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,1,1,5,
        1,14,8,1,10,1,12,1,17,9,1,1,2,4,2,20,8,2,11,2,12,2,21,1,3,4,3,25,
        8,3,11,3,12,3,26,1,3,1,3,0,0,4,1,1,3,2,5,3,7,4,1,0,4,3,0,65,90,95,
        95,97,122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,
        32,32,32,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,1,9,1,0,
        0,0,3,11,1,0,0,0,5,19,1,0,0,0,7,24,1,0,0,0,9,10,5,61,0,0,10,2,1,
        0,0,0,11,15,7,0,0,0,12,14,7,1,0,0,13,12,1,0,0,0,14,17,1,0,0,0,15,
        13,1,0,0,0,15,16,1,0,0,0,16,4,1,0,0,0,17,15,1,0,0,0,18,20,7,2,0,
        0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,6,1,
        0,0,0,23,25,7,3,0,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,
        27,1,0,0,0,27,28,1,0,0,0,28,29,6,3,0,0,29,8,1,0,0,0,4,0,15,21,26,
        1,6,0,0
    ]

class PythonParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
    NUMBER = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "ID", "NUMBER", "WS" ]

    grammarFileName = "PythonParser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


