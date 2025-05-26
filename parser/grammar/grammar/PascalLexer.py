# Generated from grammar/PascalLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,53,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,5,4,42,8,4,10,4,12,
        4,45,9,4,1,5,4,5,48,8,5,11,5,12,5,49,1,5,1,5,0,0,6,1,1,3,2,5,3,7,
        4,9,5,11,6,1,0,3,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,
        122,3,0,9,10,13,13,32,32,54,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,21,1,0,0,0,5,
        27,1,0,0,0,7,31,1,0,0,0,9,39,1,0,0,0,11,47,1,0,0,0,13,14,5,112,0,
        0,14,15,5,114,0,0,15,16,5,111,0,0,16,17,5,103,0,0,17,18,5,114,0,
        0,18,19,5,97,0,0,19,20,5,109,0,0,20,2,1,0,0,0,21,22,5,98,0,0,22,
        23,5,101,0,0,23,24,5,103,0,0,24,25,5,105,0,0,25,26,5,110,0,0,26,
        4,1,0,0,0,27,28,5,101,0,0,28,29,5,110,0,0,29,30,5,100,0,0,30,6,1,
        0,0,0,31,32,5,119,0,0,32,33,5,114,0,0,33,34,5,105,0,0,34,35,5,116,
        0,0,35,36,5,101,0,0,36,37,5,108,0,0,37,38,5,110,0,0,38,8,1,0,0,0,
        39,43,7,0,0,0,40,42,7,1,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,
        0,0,0,43,44,1,0,0,0,44,10,1,0,0,0,45,43,1,0,0,0,46,48,7,2,0,0,47,
        46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,
        0,51,52,6,5,0,0,52,12,1,0,0,0,3,0,43,49,1,6,0,0
    ]

class PascalLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROGRAM = 1
    BEGIN = 2
    END = 3
    WRITELN = 4
    IDENTIFIER = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'program'", "'begin'", "'end'", "'writeln'" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM", "BEGIN", "END", "WRITELN", "IDENTIFIER", "WS" ]

    ruleNames = [ "PROGRAM", "BEGIN", "END", "WRITELN", "IDENTIFIER", "WS" ]

    grammarFileName = "PascalLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


