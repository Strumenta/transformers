# Generated from PLIParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PLIParser import PLIParser
else:
    from PLIParser import PLIParser

# This class defines a complete listener for a parse tree produced by PLIParser.
class PLIParserListener(ParseTreeListener):

    # Enter a parse tree produced by PLIParser#program.
    def enterProgram(self, ctx:PLIParser.ProgramContext):
        pass

    # Exit a parse tree produced by PLIParser#program.
    def exitProgram(self, ctx:PLIParser.ProgramContext):
        pass


    # Enter a parse tree produced by PLIParser#stmt.
    def enterStmt(self, ctx:PLIParser.StmtContext):
        pass

    # Exit a parse tree produced by PLIParser#stmt.
    def exitStmt(self, ctx:PLIParser.StmtContext):
        pass


    # Enter a parse tree produced by PLIParser#comment.
    def enterComment(self, ctx:PLIParser.CommentContext):
        pass

    # Exit a parse tree produced by PLIParser#comment.
    def exitComment(self, ctx:PLIParser.CommentContext):
        pass


    # Enter a parse tree produced by PLIParser#label.
    def enterLabel(self, ctx:PLIParser.LabelContext):
        pass

    # Exit a parse tree produced by PLIParser#label.
    def exitLabel(self, ctx:PLIParser.LabelContext):
        pass


    # Enter a parse tree produced by PLIParser#statement.
    def enterStatement(self, ctx:PLIParser.StatementContext):
        pass

    # Exit a parse tree produced by PLIParser#statement.
    def exitStatement(self, ctx:PLIParser.StatementContext):
        pass


    # Enter a parse tree produced by PLIParser#nopStmt.
    def enterNopStmt(self, ctx:PLIParser.NopStmtContext):
        pass

    # Exit a parse tree produced by PLIParser#nopStmt.
    def exitNopStmt(self, ctx:PLIParser.NopStmtContext):
        pass


    # Enter a parse tree produced by PLIParser#assignStmt.
    def enterAssignStmt(self, ctx:PLIParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by PLIParser#assignStmt.
    def exitAssignStmt(self, ctx:PLIParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by PLIParser#assignByName.
    def enterAssignByName(self, ctx:PLIParser.AssignByNameContext):
        pass

    # Exit a parse tree produced by PLIParser#assignByName.
    def exitAssignByName(self, ctx:PLIParser.AssignByNameContext):
        pass


    # Enter a parse tree produced by PLIParser#declareStmt.
    def enterDeclareStmt(self, ctx:PLIParser.DeclareStmtContext):
        pass

    # Exit a parse tree produced by PLIParser#declareStmt.
    def exitDeclareStmt(self, ctx:PLIParser.DeclareStmtContext):
        pass


    # Enter a parse tree produced by PLIParser#declaration.
    def enterDeclaration(self, ctx:PLIParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PLIParser#declaration.
    def exitDeclaration(self, ctx:PLIParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PLIParser#level.
    def enterLevel(self, ctx:PLIParser.LevelContext):
        pass

    # Exit a parse tree produced by PLIParser#level.
    def exitLevel(self, ctx:PLIParser.LevelContext):
        pass


    # Enter a parse tree produced by PLIParser#name.
    def enterName(self, ctx:PLIParser.NameContext):
        pass

    # Exit a parse tree produced by PLIParser#name.
    def exitName(self, ctx:PLIParser.NameContext):
        pass


    # Enter a parse tree produced by PLIParser#factoredNames.
    def enterFactoredNames(self, ctx:PLIParser.FactoredNamesContext):
        pass

    # Exit a parse tree produced by PLIParser#factoredNames.
    def exitFactoredNames(self, ctx:PLIParser.FactoredNamesContext):
        pass


    # Enter a parse tree produced by PLIParser#attributes.
    def enterAttributes(self, ctx:PLIParser.AttributesContext):
        pass

    # Exit a parse tree produced by PLIParser#attributes.
    def exitAttributes(self, ctx:PLIParser.AttributesContext):
        pass


    # Enter a parse tree produced by PLIParser#data.
    def enterData(self, ctx:PLIParser.DataContext):
        pass

    # Exit a parse tree produced by PLIParser#data.
    def exitData(self, ctx:PLIParser.DataContext):
        pass


    # Enter a parse tree produced by PLIParser#precision.
    def enterPrecision(self, ctx:PLIParser.PrecisionContext):
        pass

    # Exit a parse tree produced by PLIParser#precision.
    def exitPrecision(self, ctx:PLIParser.PrecisionContext):
        pass


    # Enter a parse tree produced by PLIParser#decimals.
    def enterDecimals(self, ctx:PLIParser.DecimalsContext):
        pass

    # Exit a parse tree produced by PLIParser#decimals.
    def exitDecimals(self, ctx:PLIParser.DecimalsContext):
        pass


    # Enter a parse tree produced by PLIParser#alignment.
    def enterAlignment(self, ctx:PLIParser.AlignmentContext):
        pass

    # Exit a parse tree produced by PLIParser#alignment.
    def exitAlignment(self, ctx:PLIParser.AlignmentContext):
        pass


    # Enter a parse tree produced by PLIParser#scope.
    def enterScope(self, ctx:PLIParser.ScopeContext):
        pass

    # Exit a parse tree produced by PLIParser#scope.
    def exitScope(self, ctx:PLIParser.ScopeContext):
        pass


    # Enter a parse tree produced by PLIParser#externalName.
    def enterExternalName(self, ctx:PLIParser.ExternalNameContext):
        pass

    # Exit a parse tree produced by PLIParser#externalName.
    def exitExternalName(self, ctx:PLIParser.ExternalNameContext):
        pass


    # Enter a parse tree produced by PLIParser#storage.
    def enterStorage(self, ctx:PLIParser.StorageContext):
        pass

    # Exit a parse tree produced by PLIParser#storage.
    def exitStorage(self, ctx:PLIParser.StorageContext):
        pass


    # Enter a parse tree produced by PLIParser#locator.
    def enterLocator(self, ctx:PLIParser.LocatorContext):
        pass

    # Exit a parse tree produced by PLIParser#locator.
    def exitLocator(self, ctx:PLIParser.LocatorContext):
        pass


    # Enter a parse tree produced by PLIParser#constant.
    def enterConstant(self, ctx:PLIParser.ConstantContext):
        pass

    # Exit a parse tree produced by PLIParser#constant.
    def exitConstant(self, ctx:PLIParser.ConstantContext):
        pass


    # Enter a parse tree produced by PLIParser#initialization.
    def enterInitialization(self, ctx:PLIParser.InitializationContext):
        pass

    # Exit a parse tree produced by PLIParser#initialization.
    def exitInitialization(self, ctx:PLIParser.InitializationContext):
        pass


    # Enter a parse tree produced by PLIParser#initSpec.
    def enterInitSpec(self, ctx:PLIParser.InitSpecContext):
        pass

    # Exit a parse tree produced by PLIParser#initSpec.
    def exitInitSpec(self, ctx:PLIParser.InitSpecContext):
        pass


    # Enter a parse tree produced by PLIParser#initValue.
    def enterInitValue(self, ctx:PLIParser.InitValueContext):
        pass

    # Exit a parse tree produced by PLIParser#initValue.
    def exitInitValue(self, ctx:PLIParser.InitValueContext):
        pass


    # Enter a parse tree produced by PLIParser#ifStmt.
    def enterIfStmt(self, ctx:PLIParser.IfStmtContext):
        pass

    # Exit a parse tree produced by PLIParser#ifStmt.
    def exitIfStmt(self, ctx:PLIParser.IfStmtContext):
        pass


    # Enter a parse tree produced by PLIParser#callStmt.
    def enterCallStmt(self, ctx:PLIParser.CallStmtContext):
        pass

    # Exit a parse tree produced by PLIParser#callStmt.
    def exitCallStmt(self, ctx:PLIParser.CallStmtContext):
        pass


    # Enter a parse tree produced by PLIParser#returnStmt.
    def enterReturnStmt(self, ctx:PLIParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by PLIParser#returnStmt.
    def exitReturnStmt(self, ctx:PLIParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by PLIParser#procedureStmt.
    def enterProcedureStmt(self, ctx:PLIParser.ProcedureStmtContext):
        pass

    # Exit a parse tree produced by PLIParser#procedureStmt.
    def exitProcedureStmt(self, ctx:PLIParser.ProcedureStmtContext):
        pass


    # Enter a parse tree produced by PLIParser#procedureParams.
    def enterProcedureParams(self, ctx:PLIParser.ProcedureParamsContext):
        pass

    # Exit a parse tree produced by PLIParser#procedureParams.
    def exitProcedureParams(self, ctx:PLIParser.ProcedureParamsContext):
        pass


    # Enter a parse tree produced by PLIParser#procedureParam.
    def enterProcedureParam(self, ctx:PLIParser.ProcedureParamContext):
        pass

    # Exit a parse tree produced by PLIParser#procedureParam.
    def exitProcedureParam(self, ctx:PLIParser.ProcedureParamContext):
        pass


    # Enter a parse tree produced by PLIParser#procedureOptions.
    def enterProcedureOptions(self, ctx:PLIParser.ProcedureOptionsContext):
        pass

    # Exit a parse tree produced by PLIParser#procedureOptions.
    def exitProcedureOptions(self, ctx:PLIParser.ProcedureOptionsContext):
        pass


    # Enter a parse tree produced by PLIParser#procedureOption.
    def enterProcedureOption(self, ctx:PLIParser.ProcedureOptionContext):
        pass

    # Exit a parse tree produced by PLIParser#procedureOption.
    def exitProcedureOption(self, ctx:PLIParser.ProcedureOptionContext):
        pass


    # Enter a parse tree produced by PLIParser#procedureReturns.
    def enterProcedureReturns(self, ctx:PLIParser.ProcedureReturnsContext):
        pass

    # Exit a parse tree produced by PLIParser#procedureReturns.
    def exitProcedureReturns(self, ctx:PLIParser.ProcedureReturnsContext):
        pass


    # Enter a parse tree produced by PLIParser#expression.
    def enterExpression(self, ctx:PLIParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PLIParser#expression.
    def exitExpression(self, ctx:PLIParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PLIParser#comparison.
    def enterComparison(self, ctx:PLIParser.ComparisonContext):
        pass

    # Exit a parse tree produced by PLIParser#comparison.
    def exitComparison(self, ctx:PLIParser.ComparisonContext):
        pass


    # Enter a parse tree produced by PLIParser#literal.
    def enterLiteral(self, ctx:PLIParser.LiteralContext):
        pass

    # Exit a parse tree produced by PLIParser#literal.
    def exitLiteral(self, ctx:PLIParser.LiteralContext):
        pass


    # Enter a parse tree produced by PLIParser#repetitionFactor.
    def enterRepetitionFactor(self, ctx:PLIParser.RepetitionFactorContext):
        pass

    # Exit a parse tree produced by PLIParser#repetitionFactor.
    def exitRepetitionFactor(self, ctx:PLIParser.RepetitionFactorContext):
        pass


    # Enter a parse tree produced by PLIParser#identifier.
    def enterIdentifier(self, ctx:PLIParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PLIParser#identifier.
    def exitIdentifier(self, ctx:PLIParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PLIParser#simpleIdentifier.
    def enterSimpleIdentifier(self, ctx:PLIParser.SimpleIdentifierContext):
        pass

    # Exit a parse tree produced by PLIParser#simpleIdentifier.
    def exitSimpleIdentifier(self, ctx:PLIParser.SimpleIdentifierContext):
        pass


    # Enter a parse tree produced by PLIParser#member.
    def enterMember(self, ctx:PLIParser.MemberContext):
        pass

    # Exit a parse tree produced by PLIParser#member.
    def exitMember(self, ctx:PLIParser.MemberContext):
        pass


    # Enter a parse tree produced by PLIParser#subscript.
    def enterSubscript(self, ctx:PLIParser.SubscriptContext):
        pass

    # Exit a parse tree produced by PLIParser#subscript.
    def exitSubscript(self, ctx:PLIParser.SubscriptContext):
        pass


    # Enter a parse tree produced by PLIParser#picture.
    def enterPicture(self, ctx:PLIParser.PictureContext):
        pass

    # Exit a parse tree produced by PLIParser#picture.
    def exitPicture(self, ctx:PLIParser.PictureContext):
        pass



del PLIParser