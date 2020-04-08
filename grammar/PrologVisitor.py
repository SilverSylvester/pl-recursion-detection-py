# Generated from .\Prolog.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrologParser import PrologParser
else:
    from PrologParser import PrologParser

# This class defines a complete generic visitor for a parse tree produced by PrologParser.

class PrologVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrologParser#p_text.
    def visitP_text(self, ctx:PrologParser.P_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#directive.
    def visitDirective(self, ctx:PrologParser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#clause.
    def visitClause(self, ctx:PrologParser.ClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#termlist.
    def visitTermlist(self, ctx:PrologParser.TermlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#atom_term.
    def visitAtom_term(self, ctx:PrologParser.Atom_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#binary_operator.
    def visitBinary_operator(self, ctx:PrologParser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#unary_operator.
    def visitUnary_operator(self, ctx:PrologParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#braced_term.
    def visitBraced_term(self, ctx:PrologParser.Braced_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#list_term.
    def visitList_term(self, ctx:PrologParser.List_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#variable.
    def visitVariable(self, ctx:PrologParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#float.
    def visitFloat(self, ctx:PrologParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#compound_term.
    def visitCompound_term(self, ctx:PrologParser.Compound_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#integer_term.
    def visitInteger_term(self, ctx:PrologParser.Integer_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#curly_bracketed_term.
    def visitCurly_bracketed_term(self, ctx:PrologParser.Curly_bracketed_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#operator.
    def visitOperator(self, ctx:PrologParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#empty_list.
    def visitEmpty_list(self, ctx:PrologParser.Empty_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#empty_braces.
    def visitEmpty_braces(self, ctx:PrologParser.Empty_bracesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#name.
    def visitName(self, ctx:PrologParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#graphic.
    def visitGraphic(self, ctx:PrologParser.GraphicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#quoted_string.
    def visitQuoted_string(self, ctx:PrologParser.Quoted_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#dq_string.
    def visitDq_string(self, ctx:PrologParser.Dq_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#backq_string.
    def visitBackq_string(self, ctx:PrologParser.Backq_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#semicolon.
    def visitSemicolon(self, ctx:PrologParser.SemicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#cut.
    def visitCut(self, ctx:PrologParser.CutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#integer.
    def visitInteger(self, ctx:PrologParser.IntegerContext):
        return self.visitChildren(ctx)



del PrologParser