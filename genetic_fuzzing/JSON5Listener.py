# Generated from JSON5.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .JSON5Parser import JSON5Parser
else:
    from JSON5Parser import JSON5Parser

# This class defines a complete listener for a parse tree produced by JSON5Parser.
class JSON5Listener(ParseTreeListener):

    # Enter a parse tree produced by JSON5Parser#json5.
    def enterJson5(self, ctx:JSON5Parser.Json5Context):
        pass

    # Exit a parse tree produced by JSON5Parser#json5.
    def exitJson5(self, ctx:JSON5Parser.Json5Context):
        pass


    # Enter a parse tree produced by JSON5Parser#obj.
    def enterObj(self, ctx:JSON5Parser.ObjContext):
        pass

    # Exit a parse tree produced by JSON5Parser#obj.
    def exitObj(self, ctx:JSON5Parser.ObjContext):
        pass


    # Enter a parse tree produced by JSON5Parser#pair.
    def enterPair(self, ctx:JSON5Parser.PairContext):
        pass

    # Exit a parse tree produced by JSON5Parser#pair.
    def exitPair(self, ctx:JSON5Parser.PairContext):
        pass


    # Enter a parse tree produced by JSON5Parser#key.
    def enterKey(self, ctx:JSON5Parser.KeyContext):
        pass

    # Exit a parse tree produced by JSON5Parser#key.
    def exitKey(self, ctx:JSON5Parser.KeyContext):
        pass


    # Enter a parse tree produced by JSON5Parser#value.
    def enterValue(self, ctx:JSON5Parser.ValueContext):
        pass

    # Exit a parse tree produced by JSON5Parser#value.
    def exitValue(self, ctx:JSON5Parser.ValueContext):
        pass


    # Enter a parse tree produced by JSON5Parser#arr.
    def enterArr(self, ctx:JSON5Parser.ArrContext):
        pass

    # Exit a parse tree produced by JSON5Parser#arr.
    def exitArr(self, ctx:JSON5Parser.ArrContext):
        pass


    # Enter a parse tree produced by JSON5Parser#number.
    def enterNumber(self, ctx:JSON5Parser.NumberContext):
        pass

    # Exit a parse tree produced by JSON5Parser#number.
    def exitNumber(self, ctx:JSON5Parser.NumberContext):
        pass



del JSON5Parser