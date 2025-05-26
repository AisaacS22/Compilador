# Generated from grammar/CPPLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,37,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,26,8,2,10,2,12,
        2,29,9,2,1,3,4,3,32,8,3,11,3,12,3,33,1,3,1,3,0,0,4,1,1,3,2,5,3,7,
        4,1,0,3,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,
        9,10,13,13,32,32,38,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,1,9,1,0,0,0,3,18,1,0,0,0,5,23,1,0,0,0,7,31,1,0,0,0,9,10,5,35,
        0,0,10,11,5,105,0,0,11,12,5,110,0,0,12,13,5,99,0,0,13,14,5,108,0,
        0,14,15,5,117,0,0,15,16,5,100,0,0,16,17,5,101,0,0,17,2,1,0,0,0,18,
        19,5,99,0,0,19,20,5,111,0,0,20,21,5,117,0,0,21,22,5,116,0,0,22,4,
        1,0,0,0,23,27,7,0,0,0,24,26,7,1,0,0,25,24,1,0,0,0,26,29,1,0,0,0,
        27,25,1,0,0,0,27,28,1,0,0,0,28,6,1,0,0,0,29,27,1,0,0,0,30,32,7,2,
        0,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,
        1,0,0,0,35,36,6,3,0,0,36,8,1,0,0,0,3,0,27,33,1,6,0,0
    ]

class CPPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INCLUDE = 1
    COUT = 2
    IDENTIFIER = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#include'", "'cout'" ]

    symbolicNames = [ "<INVALID>",
            "INCLUDE", "COUT", "IDENTIFIER", "WS" ]

    ruleNames = [ "INCLUDE", "COUT", "IDENTIFIER", "WS" ]

    grammarFileName = "CPPLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


