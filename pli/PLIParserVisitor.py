# Generated from PLIParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PLIParser import PLIParser
else:
    from PLIParser import PLIParser

# This class defines a complete generic visitor for a parse tree produced by PLIParser.

class PLIParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLIParser#program.
    def visitProgram(self, ctx:PLIParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#stmt.
    def visitStmt(self, ctx:PLIParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#comment.
    def visitComment(self, ctx:PLIParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#label.
    def visitLabel(self, ctx:PLIParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#statement.
    def visitStatement(self, ctx:PLIParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#nopStmt.
    def visitNopStmt(self, ctx:PLIParser.NopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#assignStmt.
    def visitAssignStmt(self, ctx:PLIParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#assignByName.
    def visitAssignByName(self, ctx:PLIParser.AssignByNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#declareStmt.
    def visitDeclareStmt(self, ctx:PLIParser.DeclareStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#declaration.
    def visitDeclaration(self, ctx:PLIParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#level.
    def visitLevel(self, ctx:PLIParser.LevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#name.
    def visitName(self, ctx:PLIParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#factoredNames.
    def visitFactoredNames(self, ctx:PLIParser.FactoredNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#attributes.
    def visitAttributes(self, ctx:PLIParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#data.
    def visitData(self, ctx:PLIParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#precision.
    def visitPrecision(self, ctx:PLIParser.PrecisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#decimals.
    def visitDecimals(self, ctx:PLIParser.DecimalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#alignment.
    def visitAlignment(self, ctx:PLIParser.AlignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#scope.
    def visitScope(self, ctx:PLIParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#externalName.
    def visitExternalName(self, ctx:PLIParser.ExternalNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#storage.
    def visitStorage(self, ctx:PLIParser.StorageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#locator.
    def visitLocator(self, ctx:PLIParser.LocatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#constant.
    def visitConstant(self, ctx:PLIParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#initialization.
    def visitInitialization(self, ctx:PLIParser.InitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#initSpec.
    def visitInitSpec(self, ctx:PLIParser.InitSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#initValue.
    def visitInitValue(self, ctx:PLIParser.InitValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ifStmt.
    def visitIfStmt(self, ctx:PLIParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#callStmt.
    def visitCallStmt(self, ctx:PLIParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#returnStmt.
    def visitReturnStmt(self, ctx:PLIParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedureStmt.
    def visitProcedureStmt(self, ctx:PLIParser.ProcedureStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedureParams.
    def visitProcedureParams(self, ctx:PLIParser.ProcedureParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedureParam.
    def visitProcedureParam(self, ctx:PLIParser.ProcedureParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedureOptions.
    def visitProcedureOptions(self, ctx:PLIParser.ProcedureOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedureOption.
    def visitProcedureOption(self, ctx:PLIParser.ProcedureOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedureReturns.
    def visitProcedureReturns(self, ctx:PLIParser.ProcedureReturnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#expression.
    def visitExpression(self, ctx:PLIParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#comparison.
    def visitComparison(self, ctx:PLIParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#literal.
    def visitLiteral(self, ctx:PLIParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#repetitionFactor.
    def visitRepetitionFactor(self, ctx:PLIParser.RepetitionFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#identifier.
    def visitIdentifier(self, ctx:PLIParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#simpleIdentifier.
    def visitSimpleIdentifier(self, ctx:PLIParser.SimpleIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#member.
    def visitMember(self, ctx:PLIParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#subscript.
    def visitSubscript(self, ctx:PLIParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#picture.
    def visitPicture(self, ctx:PLIParser.PictureContext):
        return self.visitChildren(ctx)



del PLIParser