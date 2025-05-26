# Generated from grammar/HTMLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HTMLParserParser import HTMLParserParser
else:
    from HTMLParserParser import HTMLParserParser

# This class defines a complete listener for a parse tree produced by HTMLParserParser.
class HTMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by HTMLParserParser#document.
    def enterDocument(self, ctx:HTMLParserParser.DocumentContext):
        pass

    # Exit a parse tree produced by HTMLParserParser#document.
    def exitDocument(self, ctx:HTMLParserParser.DocumentContext):
        pass


    # Enter a parse tree produced by HTMLParserParser#element.
    def enterElement(self, ctx:HTMLParserParser.ElementContext):
        pass

    # Exit a parse tree produced by HTMLParserParser#element.
    def exitElement(self, ctx:HTMLParserParser.ElementContext):
        pass


    # Enter a parse tree produced by HTMLParserParser#open_tag.
    def enterOpen_tag(self, ctx:HTMLParserParser.Open_tagContext):
        pass

    # Exit a parse tree produced by HTMLParserParser#open_tag.
    def exitOpen_tag(self, ctx:HTMLParserParser.Open_tagContext):
        pass


    # Enter a parse tree produced by HTMLParserParser#close_tag.
    def enterClose_tag(self, ctx:HTMLParserParser.Close_tagContext):
        pass

    # Exit a parse tree produced by HTMLParserParser#close_tag.
    def exitClose_tag(self, ctx:HTMLParserParser.Close_tagContext):
        pass


    # Enter a parse tree produced by HTMLParserParser#content.
    def enterContent(self, ctx:HTMLParserParser.ContentContext):
        pass

    # Exit a parse tree produced by HTMLParserParser#content.
    def exitContent(self, ctx:HTMLParserParser.ContentContext):
        pass



del HTMLParserParser