from pli.PLIParser import PLIParser

from pli.PLIParserVisitor import PLIParserVisitor


class PLIVisitor(PLIParserVisitor):

    def __init__(self):
        self.label = None
        self.scope = []
        self.statements = []

    def enterScope(self):
        self.scope.append({})

    def exitScope(self):
        self.scope.pop()

    def currentScope(self):
        return self.scope[-1]

    def decodeType(self, attributes):
        for attr in attributes:
            if attr.data().FIXED() is not None:
                return "Int"
            if attr.data().CHARACTER() is not None:
                return "String"
        return ""

    # Visit a parse tree produced by PLIParser#program.
    def visitProgram(self, ctx: PLIParser.ProgramContext):

        for i in range(len(ctx.stmt())):
            self.visitStmt(ctx.stmt(i))

        return self.statements

    # Visit a parse tree produced by PLIParser#stmt.
    def visitStmt(self, ctx: PLIParser.StmtContext):
        self.label = None
        if ctx.label() is not None:
            self.label = ctx.label().getText()
            self.label = self.label[:-1]
            self.label = self.label.lower()

        self.visitStatement(ctx.statement())

    # Visit a parse tree produced by PLIParser#stmt.
    def visitStatement(self, ctx: PLIParser.StatementContext):
        symbols = {}
        if ctx.procedureStmt() is not None:
            self.enterScope()
            tokens = ["PROCEDURE"]
            # check the options
            if ctx.procedureStmt().procedureOptions() is not None:
                for option in ctx.procedureStmt().procedureOptions().procedureOption():
                    if option.MAIN() is not None:
                        tokens.append("MAIN")
                        tokens.append("{{type0}}")
                        tokens.append("{{type1}}")
                        symbols = {"type0": "Array", "type1": "String"}
            else:
                tokens.append("{{name}}")
                symbols = {"name": self.label}

            if ctx.procedureStmt().procedureParams() is not None:
                index = 0
                for param in ctx.procedureStmt().procedureParams().procedureParam():
                    self.scope[-1][param.getText().lower()] = "Int"
                    tokens.append("{{param" + str(index) + "}}")
                    tokens.append("{{type" + str(index) + "}}")
                    tokens.append("{{return}}")
                    symbols["param" + str(index)] = param.getText().lower()
                    symbols["type" + str(index)] = "Int"
                    symbols["return"] = "Int"
                    index += 1

            self.statements.append({
                "pli": tokens,
                "context": symbols
            })

            # add the synthetic token
            self.statements.append({
                "pli": ["DO"],
                "context": {}
            })
            # process the procedure body
            for stmt in ctx.procedureStmt().stmt():
                self.visitStmt(stmt)
            # add the end
            self.statements.append({
                "pli": ["END"],
                "context": {}
            })
            self.exitScope()

        if ctx.declareStmt() is not None:
            index = 0

            for decl in ctx.declareStmt().declaration():
                type = self.decodeType(decl.attributes())
                if decl.name().factoredNames() is not None:
                    for name in decl.name().factoredNames().identifier():
                        tokens = ["DECLARE"]
                        if not name.getText().lower() in self.currentScope().keys():
                            tokens.append("name")
                            context = {
                                'name': name.getText().lower(),
                                'type': type,
                            }

                            self.statements.append({
                                "pli": tokens,
                                "context": context
                            })
                        else:
                            self.currentScope()[name.getText().lower()] = type
                        index += 1
                else:
                    tokens = ["DECLARE"]
                    if not decl.name().getText().lower() in self.currentScope().keys():
                        tokens.append("name")
                        context = {
                            'name': decl.name().getText().lower(),
                            'type': type,
                        }

                        self.statements.append({
                            "pli": tokens,
                            "context": context
                        })
                    else:
                        self.currentScope()[decl.name().getText().lower()] = type

        if ctx.assignStmt() is not None:
            tokens = ["ASSIGN", "{{name}}", "{{value}}"]
            context = {
                "name": ctx.assignStmt().identifier(0).getText().lower(),
                "value": ctx.assignStmt().expression().getText().lower()
            }
            self.statements.append({
                "pli": tokens,
                "context": context
            })

        if ctx.callStmt() is not None:
            tokens = ["CALL", "{{name}}"]
            context = {
                "name": ctx.callStmt().IDENTIFIER().getText().lower(),
            }
            self.statements.append({
                "pli": tokens,
                "context": context
            })

        if ctx.returnStmt() is not None:
            tokens = ["RETURN", "{{value}}"]
            context = {
                "value": ctx.returnStmt().expression().getText().lower(),
            }
            self.statements.append({
                "pli": tokens,
                "context": context
            })

        if ctx.ifStmt() is not None:
            tokens = ["IF", "{{value}}", "THEN"]
            context = {
                "value": ctx.ifStmt().expression().getText().lower(),
            }
            self.statements.append({
                "pli": tokens,
                "context": context
            })
            self.statements.append({
                "pli": ["DO"],
                "context": {}
            })
            self.visitStmt(ctx.ifStmt().stmt())
            self.statements.append({
                "pli": ["END"],
                "context": {}
            })
        return symbols
