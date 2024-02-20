# Generated from JSON5.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .JSON5Parser import JSON5Parser
else:
    from JSON5Parser import JSON5Parser

# This class defines a complete generic visitor for a parse tree produced by JSON5Parser.

class JSON5Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by JSON5Parser#json5.
    def visitJson5(self, ctx:JSON5Parser.Json5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSON5Parser#obj.
    def visitObj(self, ctx:JSON5Parser.ObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSON5Parser#pair.
    def visitPair(self, ctx:JSON5Parser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSON5Parser#key.
    def visitKey(self, ctx:JSON5Parser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSON5Parser#value.
    def visitValue(self, ctx:JSON5Parser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSON5Parser#arr.
    def visitArr(self, ctx:JSON5Parser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSON5Parser#number.
    def visitNumber(self, ctx:JSON5Parser.NumberContext):
        return self.visitChildren(ctx)



del JSON5Parser