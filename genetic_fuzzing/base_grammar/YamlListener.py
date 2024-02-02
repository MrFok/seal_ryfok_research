# Generated from Yaml.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .YamlParser import YamlParser
else:
    from YamlParser import YamlParser

# This class defines a complete listener for a parse tree produced by YamlParser.
class YamlListener(ParseTreeListener):

    # Enter a parse tree produced by YamlParser#statement.
    def enterStatement(self, ctx:YamlParser.StatementContext):
        pass

    # Exit a parse tree produced by YamlParser#statement.
    def exitStatement(self, ctx:YamlParser.StatementContext):
        pass


    # Enter a parse tree produced by YamlParser#file.
    def enterFile(self, ctx:YamlParser.FileContext):
        pass

    # Exit a parse tree produced by YamlParser#file.
    def exitFile(self, ctx:YamlParser.FileContext):
        pass


    # Enter a parse tree produced by YamlParser#object.
    def enterObject(self, ctx:YamlParser.ObjectContext):
        pass

    # Exit a parse tree produced by YamlParser#object.
    def exitObject(self, ctx:YamlParser.ObjectContext):
        pass


    # Enter a parse tree produced by YamlParser#objectbody.
    def enterObjectbody(self, ctx:YamlParser.ObjectbodyContext):
        pass

    # Exit a parse tree produced by YamlParser#objectbody.
    def exitObjectbody(self, ctx:YamlParser.ObjectbodyContext):
        pass


    # Enter a parse tree produced by YamlParser#file2.
    def enterFile2(self, ctx:YamlParser.File2Context):
        pass

    # Exit a parse tree produced by YamlParser#file2.
    def exitFile2(self, ctx:YamlParser.File2Context):
        pass


    # Enter a parse tree produced by YamlParser#list.
    def enterList(self, ctx:YamlParser.ListContext):
        pass

    # Exit a parse tree produced by YamlParser#list.
    def exitList(self, ctx:YamlParser.ListContext):
        pass


    # Enter a parse tree produced by YamlParser#listitem.
    def enterListitem(self, ctx:YamlParser.ListitemContext):
        pass

    # Exit a parse tree produced by YamlParser#listitem.
    def exitListitem(self, ctx:YamlParser.ListitemContext):
        pass


    # Enter a parse tree produced by YamlParser#mappinglist.
    def enterMappinglist(self, ctx:YamlParser.MappinglistContext):
        pass

    # Exit a parse tree produced by YamlParser#mappinglist.
    def exitMappinglist(self, ctx:YamlParser.MappinglistContext):
        pass


    # Enter a parse tree produced by YamlParser#key.
    def enterKey(self, ctx:YamlParser.KeyContext):
        pass

    # Exit a parse tree produced by YamlParser#key.
    def exitKey(self, ctx:YamlParser.KeyContext):
        pass


    # Enter a parse tree produced by YamlParser#value.
    def enterValue(self, ctx:YamlParser.ValueContext):
        pass

    # Exit a parse tree produced by YamlParser#value.
    def exitValue(self, ctx:YamlParser.ValueContext):
        pass


    # Enter a parse tree produced by YamlParser#mapping.
    def enterMapping(self, ctx:YamlParser.MappingContext):
        pass

    # Exit a parse tree produced by YamlParser#mapping.
    def exitMapping(self, ctx:YamlParser.MappingContext):
        pass


    # Enter a parse tree produced by YamlParser#single_input.
    def enterSingle_input(self, ctx:YamlParser.Single_inputContext):
        pass

    # Exit a parse tree produced by YamlParser#single_input.
    def exitSingle_input(self, ctx:YamlParser.Single_inputContext):
        pass


    # Enter a parse tree produced by YamlParser#file_input.
    def enterFile_input(self, ctx:YamlParser.File_inputContext):
        pass

    # Exit a parse tree produced by YamlParser#file_input.
    def exitFile_input(self, ctx:YamlParser.File_inputContext):
        pass


    # Enter a parse tree produced by YamlParser#eval_input.
    def enterEval_input(self, ctx:YamlParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by YamlParser#eval_input.
    def exitEval_input(self, ctx:YamlParser.Eval_inputContext):
        pass


    # Enter a parse tree produced by YamlParser#decorator.
    def enterDecorator(self, ctx:YamlParser.DecoratorContext):
        pass

    # Exit a parse tree produced by YamlParser#decorator.
    def exitDecorator(self, ctx:YamlParser.DecoratorContext):
        pass


    # Enter a parse tree produced by YamlParser#decorators.
    def enterDecorators(self, ctx:YamlParser.DecoratorsContext):
        pass

    # Exit a parse tree produced by YamlParser#decorators.
    def exitDecorators(self, ctx:YamlParser.DecoratorsContext):
        pass


    # Enter a parse tree produced by YamlParser#decorated.
    def enterDecorated(self, ctx:YamlParser.DecoratedContext):
        pass

    # Exit a parse tree produced by YamlParser#decorated.
    def exitDecorated(self, ctx:YamlParser.DecoratedContext):
        pass


    # Enter a parse tree produced by YamlParser#funcdef.
    def enterFuncdef(self, ctx:YamlParser.FuncdefContext):
        pass

    # Exit a parse tree produced by YamlParser#funcdef.
    def exitFuncdef(self, ctx:YamlParser.FuncdefContext):
        pass


    # Enter a parse tree produced by YamlParser#parameters.
    def enterParameters(self, ctx:YamlParser.ParametersContext):
        pass

    # Exit a parse tree produced by YamlParser#parameters.
    def exitParameters(self, ctx:YamlParser.ParametersContext):
        pass


    # Enter a parse tree produced by YamlParser#typedargslist.
    def enterTypedargslist(self, ctx:YamlParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by YamlParser#typedargslist.
    def exitTypedargslist(self, ctx:YamlParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by YamlParser#tfpdef.
    def enterTfpdef(self, ctx:YamlParser.TfpdefContext):
        pass

    # Exit a parse tree produced by YamlParser#tfpdef.
    def exitTfpdef(self, ctx:YamlParser.TfpdefContext):
        pass


    # Enter a parse tree produced by YamlParser#varargslist.
    def enterVarargslist(self, ctx:YamlParser.VarargslistContext):
        pass

    # Exit a parse tree produced by YamlParser#varargslist.
    def exitVarargslist(self, ctx:YamlParser.VarargslistContext):
        pass


    # Enter a parse tree produced by YamlParser#vfpdef.
    def enterVfpdef(self, ctx:YamlParser.VfpdefContext):
        pass

    # Exit a parse tree produced by YamlParser#vfpdef.
    def exitVfpdef(self, ctx:YamlParser.VfpdefContext):
        pass


    # Enter a parse tree produced by YamlParser#stmt.
    def enterStmt(self, ctx:YamlParser.StmtContext):
        pass

    # Exit a parse tree produced by YamlParser#stmt.
    def exitStmt(self, ctx:YamlParser.StmtContext):
        pass


    # Enter a parse tree produced by YamlParser#simple_stmt.
    def enterSimple_stmt(self, ctx:YamlParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#simple_stmt.
    def exitSimple_stmt(self, ctx:YamlParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#small_stmt.
    def enterSmall_stmt(self, ctx:YamlParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#small_stmt.
    def exitSmall_stmt(self, ctx:YamlParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#expr_stmt.
    def enterExpr_stmt(self, ctx:YamlParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#expr_stmt.
    def exitExpr_stmt(self, ctx:YamlParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:YamlParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by YamlParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:YamlParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by YamlParser#augassign.
    def enterAugassign(self, ctx:YamlParser.AugassignContext):
        pass

    # Exit a parse tree produced by YamlParser#augassign.
    def exitAugassign(self, ctx:YamlParser.AugassignContext):
        pass


    # Enter a parse tree produced by YamlParser#del_stmt.
    def enterDel_stmt(self, ctx:YamlParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#del_stmt.
    def exitDel_stmt(self, ctx:YamlParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#pass_stmt.
    def enterPass_stmt(self, ctx:YamlParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#pass_stmt.
    def exitPass_stmt(self, ctx:YamlParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#flow_stmt.
    def enterFlow_stmt(self, ctx:YamlParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#flow_stmt.
    def exitFlow_stmt(self, ctx:YamlParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#break_stmt.
    def enterBreak_stmt(self, ctx:YamlParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#break_stmt.
    def exitBreak_stmt(self, ctx:YamlParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#continue_stmt.
    def enterContinue_stmt(self, ctx:YamlParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#continue_stmt.
    def exitContinue_stmt(self, ctx:YamlParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#return_stmt.
    def enterReturn_stmt(self, ctx:YamlParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#return_stmt.
    def exitReturn_stmt(self, ctx:YamlParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#yield_stmt.
    def enterYield_stmt(self, ctx:YamlParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#yield_stmt.
    def exitYield_stmt(self, ctx:YamlParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#raise_stmt.
    def enterRaise_stmt(self, ctx:YamlParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#raise_stmt.
    def exitRaise_stmt(self, ctx:YamlParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#import_stmt.
    def enterImport_stmt(self, ctx:YamlParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#import_stmt.
    def exitImport_stmt(self, ctx:YamlParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#import_name.
    def enterImport_name(self, ctx:YamlParser.Import_nameContext):
        pass

    # Exit a parse tree produced by YamlParser#import_name.
    def exitImport_name(self, ctx:YamlParser.Import_nameContext):
        pass


    # Enter a parse tree produced by YamlParser#import_from.
    def enterImport_from(self, ctx:YamlParser.Import_fromContext):
        pass

    # Exit a parse tree produced by YamlParser#import_from.
    def exitImport_from(self, ctx:YamlParser.Import_fromContext):
        pass


    # Enter a parse tree produced by YamlParser#import_as_name.
    def enterImport_as_name(self, ctx:YamlParser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by YamlParser#import_as_name.
    def exitImport_as_name(self, ctx:YamlParser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by YamlParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:YamlParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by YamlParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:YamlParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by YamlParser#import_as_names.
    def enterImport_as_names(self, ctx:YamlParser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by YamlParser#import_as_names.
    def exitImport_as_names(self, ctx:YamlParser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by YamlParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:YamlParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by YamlParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:YamlParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by YamlParser#dotted_name.
    def enterDotted_name(self, ctx:YamlParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by YamlParser#dotted_name.
    def exitDotted_name(self, ctx:YamlParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by YamlParser#global_stmt.
    def enterGlobal_stmt(self, ctx:YamlParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#global_stmt.
    def exitGlobal_stmt(self, ctx:YamlParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:YamlParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:YamlParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#assert_stmt.
    def enterAssert_stmt(self, ctx:YamlParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#assert_stmt.
    def exitAssert_stmt(self, ctx:YamlParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#compound_stmt.
    def enterCompound_stmt(self, ctx:YamlParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#compound_stmt.
    def exitCompound_stmt(self, ctx:YamlParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#if_stmt.
    def enterIf_stmt(self, ctx:YamlParser.If_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#if_stmt.
    def exitIf_stmt(self, ctx:YamlParser.If_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#while_stmt.
    def enterWhile_stmt(self, ctx:YamlParser.While_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#while_stmt.
    def exitWhile_stmt(self, ctx:YamlParser.While_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#for_stmt.
    def enterFor_stmt(self, ctx:YamlParser.For_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#for_stmt.
    def exitFor_stmt(self, ctx:YamlParser.For_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#try_stmt.
    def enterTry_stmt(self, ctx:YamlParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#try_stmt.
    def exitTry_stmt(self, ctx:YamlParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#with_stmt.
    def enterWith_stmt(self, ctx:YamlParser.With_stmtContext):
        pass

    # Exit a parse tree produced by YamlParser#with_stmt.
    def exitWith_stmt(self, ctx:YamlParser.With_stmtContext):
        pass


    # Enter a parse tree produced by YamlParser#with_item.
    def enterWith_item(self, ctx:YamlParser.With_itemContext):
        pass

    # Exit a parse tree produced by YamlParser#with_item.
    def exitWith_item(self, ctx:YamlParser.With_itemContext):
        pass


    # Enter a parse tree produced by YamlParser#except_clause.
    def enterExcept_clause(self, ctx:YamlParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by YamlParser#except_clause.
    def exitExcept_clause(self, ctx:YamlParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by YamlParser#suite.
    def enterSuite(self, ctx:YamlParser.SuiteContext):
        pass

    # Exit a parse tree produced by YamlParser#suite.
    def exitSuite(self, ctx:YamlParser.SuiteContext):
        pass


    # Enter a parse tree produced by YamlParser#test.
    def enterTest(self, ctx:YamlParser.TestContext):
        pass

    # Exit a parse tree produced by YamlParser#test.
    def exitTest(self, ctx:YamlParser.TestContext):
        pass


    # Enter a parse tree produced by YamlParser#test_nocond.
    def enterTest_nocond(self, ctx:YamlParser.Test_nocondContext):
        pass

    # Exit a parse tree produced by YamlParser#test_nocond.
    def exitTest_nocond(self, ctx:YamlParser.Test_nocondContext):
        pass


    # Enter a parse tree produced by YamlParser#lambdef.
    def enterLambdef(self, ctx:YamlParser.LambdefContext):
        pass

    # Exit a parse tree produced by YamlParser#lambdef.
    def exitLambdef(self, ctx:YamlParser.LambdefContext):
        pass


    # Enter a parse tree produced by YamlParser#lambdef_nocond.
    def enterLambdef_nocond(self, ctx:YamlParser.Lambdef_nocondContext):
        pass

    # Exit a parse tree produced by YamlParser#lambdef_nocond.
    def exitLambdef_nocond(self, ctx:YamlParser.Lambdef_nocondContext):
        pass


    # Enter a parse tree produced by YamlParser#or_test.
    def enterOr_test(self, ctx:YamlParser.Or_testContext):
        pass

    # Exit a parse tree produced by YamlParser#or_test.
    def exitOr_test(self, ctx:YamlParser.Or_testContext):
        pass


    # Enter a parse tree produced by YamlParser#and_test.
    def enterAnd_test(self, ctx:YamlParser.And_testContext):
        pass

    # Exit a parse tree produced by YamlParser#and_test.
    def exitAnd_test(self, ctx:YamlParser.And_testContext):
        pass


    # Enter a parse tree produced by YamlParser#not_test.
    def enterNot_test(self, ctx:YamlParser.Not_testContext):
        pass

    # Exit a parse tree produced by YamlParser#not_test.
    def exitNot_test(self, ctx:YamlParser.Not_testContext):
        pass


    # Enter a parse tree produced by YamlParser#comparison.
    def enterComparison(self, ctx:YamlParser.ComparisonContext):
        pass

    # Exit a parse tree produced by YamlParser#comparison.
    def exitComparison(self, ctx:YamlParser.ComparisonContext):
        pass


    # Enter a parse tree produced by YamlParser#comp_op.
    def enterComp_op(self, ctx:YamlParser.Comp_opContext):
        pass

    # Exit a parse tree produced by YamlParser#comp_op.
    def exitComp_op(self, ctx:YamlParser.Comp_opContext):
        pass


    # Enter a parse tree produced by YamlParser#star_expr.
    def enterStar_expr(self, ctx:YamlParser.Star_exprContext):
        pass

    # Exit a parse tree produced by YamlParser#star_expr.
    def exitStar_expr(self, ctx:YamlParser.Star_exprContext):
        pass


    # Enter a parse tree produced by YamlParser#expr.
    def enterExpr(self, ctx:YamlParser.ExprContext):
        pass

    # Exit a parse tree produced by YamlParser#expr.
    def exitExpr(self, ctx:YamlParser.ExprContext):
        pass


    # Enter a parse tree produced by YamlParser#xor_expr.
    def enterXor_expr(self, ctx:YamlParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by YamlParser#xor_expr.
    def exitXor_expr(self, ctx:YamlParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by YamlParser#and_expr.
    def enterAnd_expr(self, ctx:YamlParser.And_exprContext):
        pass

    # Exit a parse tree produced by YamlParser#and_expr.
    def exitAnd_expr(self, ctx:YamlParser.And_exprContext):
        pass


    # Enter a parse tree produced by YamlParser#shift_expr.
    def enterShift_expr(self, ctx:YamlParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by YamlParser#shift_expr.
    def exitShift_expr(self, ctx:YamlParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by YamlParser#arith_expr.
    def enterArith_expr(self, ctx:YamlParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by YamlParser#arith_expr.
    def exitArith_expr(self, ctx:YamlParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by YamlParser#term.
    def enterTerm(self, ctx:YamlParser.TermContext):
        pass

    # Exit a parse tree produced by YamlParser#term.
    def exitTerm(self, ctx:YamlParser.TermContext):
        pass


    # Enter a parse tree produced by YamlParser#factor.
    def enterFactor(self, ctx:YamlParser.FactorContext):
        pass

    # Exit a parse tree produced by YamlParser#factor.
    def exitFactor(self, ctx:YamlParser.FactorContext):
        pass


    # Enter a parse tree produced by YamlParser#power.
    def enterPower(self, ctx:YamlParser.PowerContext):
        pass

    # Exit a parse tree produced by YamlParser#power.
    def exitPower(self, ctx:YamlParser.PowerContext):
        pass


    # Enter a parse tree produced by YamlParser#atom.
    def enterAtom(self, ctx:YamlParser.AtomContext):
        pass

    # Exit a parse tree produced by YamlParser#atom.
    def exitAtom(self, ctx:YamlParser.AtomContext):
        pass


    # Enter a parse tree produced by YamlParser#testlist_comp.
    def enterTestlist_comp(self, ctx:YamlParser.Testlist_compContext):
        pass

    # Exit a parse tree produced by YamlParser#testlist_comp.
    def exitTestlist_comp(self, ctx:YamlParser.Testlist_compContext):
        pass


    # Enter a parse tree produced by YamlParser#trailer.
    def enterTrailer(self, ctx:YamlParser.TrailerContext):
        pass

    # Exit a parse tree produced by YamlParser#trailer.
    def exitTrailer(self, ctx:YamlParser.TrailerContext):
        pass


    # Enter a parse tree produced by YamlParser#subscriptlist.
    def enterSubscriptlist(self, ctx:YamlParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by YamlParser#subscriptlist.
    def exitSubscriptlist(self, ctx:YamlParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by YamlParser#subscript.
    def enterSubscript(self, ctx:YamlParser.SubscriptContext):
        pass

    # Exit a parse tree produced by YamlParser#subscript.
    def exitSubscript(self, ctx:YamlParser.SubscriptContext):
        pass


    # Enter a parse tree produced by YamlParser#sliceop.
    def enterSliceop(self, ctx:YamlParser.SliceopContext):
        pass

    # Exit a parse tree produced by YamlParser#sliceop.
    def exitSliceop(self, ctx:YamlParser.SliceopContext):
        pass


    # Enter a parse tree produced by YamlParser#exprlist.
    def enterExprlist(self, ctx:YamlParser.ExprlistContext):
        pass

    # Exit a parse tree produced by YamlParser#exprlist.
    def exitExprlist(self, ctx:YamlParser.ExprlistContext):
        pass


    # Enter a parse tree produced by YamlParser#testlist.
    def enterTestlist(self, ctx:YamlParser.TestlistContext):
        pass

    # Exit a parse tree produced by YamlParser#testlist.
    def exitTestlist(self, ctx:YamlParser.TestlistContext):
        pass


    # Enter a parse tree produced by YamlParser#dictorsetmaker.
    def enterDictorsetmaker(self, ctx:YamlParser.DictorsetmakerContext):
        pass

    # Exit a parse tree produced by YamlParser#dictorsetmaker.
    def exitDictorsetmaker(self, ctx:YamlParser.DictorsetmakerContext):
        pass


    # Enter a parse tree produced by YamlParser#classdef.
    def enterClassdef(self, ctx:YamlParser.ClassdefContext):
        pass

    # Exit a parse tree produced by YamlParser#classdef.
    def exitClassdef(self, ctx:YamlParser.ClassdefContext):
        pass


    # Enter a parse tree produced by YamlParser#arglist.
    def enterArglist(self, ctx:YamlParser.ArglistContext):
        pass

    # Exit a parse tree produced by YamlParser#arglist.
    def exitArglist(self, ctx:YamlParser.ArglistContext):
        pass


    # Enter a parse tree produced by YamlParser#argument.
    def enterArgument(self, ctx:YamlParser.ArgumentContext):
        pass

    # Exit a parse tree produced by YamlParser#argument.
    def exitArgument(self, ctx:YamlParser.ArgumentContext):
        pass


    # Enter a parse tree produced by YamlParser#comp_iter.
    def enterComp_iter(self, ctx:YamlParser.Comp_iterContext):
        pass

    # Exit a parse tree produced by YamlParser#comp_iter.
    def exitComp_iter(self, ctx:YamlParser.Comp_iterContext):
        pass


    # Enter a parse tree produced by YamlParser#comp_for.
    def enterComp_for(self, ctx:YamlParser.Comp_forContext):
        pass

    # Exit a parse tree produced by YamlParser#comp_for.
    def exitComp_for(self, ctx:YamlParser.Comp_forContext):
        pass


    # Enter a parse tree produced by YamlParser#comp_if.
    def enterComp_if(self, ctx:YamlParser.Comp_ifContext):
        pass

    # Exit a parse tree produced by YamlParser#comp_if.
    def exitComp_if(self, ctx:YamlParser.Comp_ifContext):
        pass


    # Enter a parse tree produced by YamlParser#yield_expr.
    def enterYield_expr(self, ctx:YamlParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by YamlParser#yield_expr.
    def exitYield_expr(self, ctx:YamlParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by YamlParser#yield_arg.
    def enterYield_arg(self, ctx:YamlParser.Yield_argContext):
        pass

    # Exit a parse tree produced by YamlParser#yield_arg.
    def exitYield_arg(self, ctx:YamlParser.Yield_argContext):
        pass


    # Enter a parse tree produced by YamlParser#string.
    def enterString(self, ctx:YamlParser.StringContext):
        pass

    # Exit a parse tree produced by YamlParser#string.
    def exitString(self, ctx:YamlParser.StringContext):
        pass


    # Enter a parse tree produced by YamlParser#number.
    def enterNumber(self, ctx:YamlParser.NumberContext):
        pass

    # Exit a parse tree produced by YamlParser#number.
    def exitNumber(self, ctx:YamlParser.NumberContext):
        pass


    # Enter a parse tree produced by YamlParser#integer.
    def enterInteger(self, ctx:YamlParser.IntegerContext):
        pass

    # Exit a parse tree produced by YamlParser#integer.
    def exitInteger(self, ctx:YamlParser.IntegerContext):
        pass



del YamlParser