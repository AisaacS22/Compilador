# Generated from grammar/TSQLLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,45,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,5,3,34,8,3,10,3,12,3,37,9,3,1,4,4,4,40,8,4,11,4,12,
        4,41,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,3,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,46,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,
        3,18,1,0,0,0,5,24,1,0,0,0,7,31,1,0,0,0,9,39,1,0,0,0,11,12,5,67,0,
        0,12,13,5,82,0,0,13,14,5,69,0,0,14,15,5,65,0,0,15,16,5,84,0,0,16,
        17,5,69,0,0,17,2,1,0,0,0,18,19,5,84,0,0,19,20,5,65,0,0,20,21,5,66,
        0,0,21,22,5,76,0,0,22,23,5,69,0,0,23,4,1,0,0,0,24,25,5,83,0,0,25,
        26,5,69,0,0,26,27,5,76,0,0,27,28,5,69,0,0,28,29,5,67,0,0,29,30,5,
        84,0,0,30,6,1,0,0,0,31,35,7,0,0,0,32,34,7,1,0,0,33,32,1,0,0,0,34,
        37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,8,1,0,0,0,37,35,1,0,0,
        0,38,40,7,2,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,43,1,0,0,0,43,44,6,4,0,0,44,10,1,0,0,0,3,0,35,41,1,6,
        0,0
    ]

class TSQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CREATE = 1
    TABLE = 2
    SELECT = 3
    IDENTIFIER = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'CREATE'", "'TABLE'", "'SELECT'" ]

    symbolicNames = [ "<INVALID>",
            "CREATE", "TABLE", "SELECT", "IDENTIFIER", "WS" ]

    ruleNames = [ "CREATE", "TABLE", "SELECT", "IDENTIFIER", "WS" ]

    grammarFileName = "TSQLLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


