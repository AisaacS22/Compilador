# Generated from grammar/HTMLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HTMLParserParser import HTMLParserParser
else:
    from HTMLParserParser import HTMLParserParser

# This class defines a complete generic visitor for a parse tree produced by HTMLParserParser.

class HTMLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HTMLParserParser#document.
    def visitDocument(self, ctx:HTMLParserParser.DocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParserParser#element.
    def visitElement(self, ctx:HTMLParserParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParserParser#open_tag.
    def visitOpen_tag(self, ctx:HTMLParserParser.Open_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParserParser#close_tag.
    def visitClose_tag(self, ctx:HTMLParserParser.Close_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParserParser#content.
    def visitContent(self, ctx:HTMLParserParser.ContentContext):
        return self.visitChildren(ctx)



del HTMLParserParser