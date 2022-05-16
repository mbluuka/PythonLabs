from importlib.util import set_loader
from operator import le
from socket import errorTab
from tkinter.messagebox import RETRY
from tokenize import Number
from turtle import goto, left, right
from typing import Literal
from rply import ParserGenerator
from ast import Eq, Gt, Load, Not, Num, SongleOp, BinryOp, Sub, TripleOp, Sum, Mul, Div, Equal, Gthan, Lthan, Gequal, Lequal, Not_equal, And_, Or_, Not_, Store_, Load_, Ifelse, While_, Eval_, Func_, Call_, operator

import sys
import re

class Parser():
    def __init__(self, module, builder, printf, struct):
        self.pg = ParserGenerator(
            ['AND','NOT','OR','IF','ELSE','WHILE','BREAK','CONTINUE','BEGIN','END',
            'INTEGER','FLOAT','FUNCTION','VAR','PROGRAM','PRINT',
            'OPEN_PAREN','CLOSE_PAREN','SEMI_COLON','COLON','COMMA',
            'EQUAL','EQUALS','NOEQUAL','MORE','LESS',
            'SUM','SUB','MUL','DIV','NUMBER','ID','LITER'],

            precedence=[
                ('left',['SUM', 'SUB']),
                ('left',['DIV','MUL'])
            ]
        )
        self.module = module
        self.builder = builder
        self.printf = printf
        self.struct = struct
    
    def parse(self):
        
        @self.pg.production('program : head globalp function main')
        def program(p):
            return p[3]
        
        @self.pg.production('head : PROGRAM ID SEMI_COLON')
        def head(p):
            pass

        @self.pg.production('globalp : declrs')
        def globalp1(p):
            return p[0]
        
        @self.pg.production('globalp : declrs globalp')
        def globalp2(p):
            return p[0], p[1]
        
        @self.pg.production('declrs : VAR ids COLON type SEMI_COLON')
        def declrs(p):
            return p[1]
        
        @self.pg.production('function : function')
        def functions2(p):
            return p[0].eval()

        @self.pg.production('function : function functions')
        def functions2(p):
            return Eval_(self.builder, self.module, p[0], p[2])
        
        @self.pg.production('function : FUNCTION ID OPEN_PAREN globalp CLOSE_PAREN COLON type SEMI_COLON BEGIN statement END')
        def finction(p):
            return Func_(self.builder, self.module, p[1], p[3], p[9])

        @self.pg.production('ids : ID')
        def ids1(p):
            return p[0]
        
        @self.pg.production('ids : ID COMMA ids')
        def ids2(p):
            return p[0], p[2]
        
        @self.pg.production('type : INTEGER')
        @self.pg.production('type : FLOAT')
        def type(p):
            return p[0]

        @self.pg.production('main : BEGIN statement END')
        def main(p):
            return p[1]
        
        @self.pg.production('statement : statement SEMI_COLON')
        def statement1(p):
            return p[0]
        
        @self.pg.production('statement : statement SEMI_COLON statement')
        def statement2(p):
            return Eval_(self.builder, self.module, p[0], p[2])
        
        @self.pg.production('statement : BREAK SEMI_COLON statement')
        def break_(p):
            global goto
            goto = "break"
            return p[2]

        @self.pg.production('statement : CONTINUE SEMI_COLON statement')
        def continue_(p):
            global goto
            goto = "continue"
            return p[2]

        @self.pg.production('statement : ID EQUALS expression')
        def equals_(p):
            return Store_(self.builder, self.module, self.struct, p[0], p[2])
        
        @self.pg.production('statement : IF OPEN_PAREN bool CLOSE_PAREN COLON BEGIN statement END')
        def if_statement(p):
            return If_(self.builder, self.module, p[2], p[6])

        @self.pg.production('statement : IF OPEN_PAREN bool CLOSE_PAREN COLON BEGIN statement END ELSE BEGIN statement END')
        def ifelse_statement(p):
            return Ifelse_(self.builder, self.module, p[2], p[6], p[10])
        
        @self.pg.production('statement : WHILE OPEN_PAREN bool CLOSE_PAREN COLON BEGIN statement END')
        def for_statement(p):
            return While_(self.builder, self.module, p[2], p[6])
        
        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def print_statement(p):
            return Print(self.builder, self.module, self.printf, p[2])
        
        @self.pg.production('statement : PRINT OPEN_PAREN LITERAL CLOSE_PAREN')
        def print_literal(p):
            return Literal_(self.builder, self.module, self.printf, p[2])
        
        @self.pg.production('bool : expression EQUAL expression')
        @self.pg.production('bool : expression GTHAN expression')
        @self.pg.production('bool : expression LTHAN expression')
        @self.pg.production('bool : expression GEQUAL expression')
        @self.pg.production('bool : expression LEQUAL expression')
        @self.pg.production('bool : expression NOT_EQUAL expression')
        def bool_compare(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            
            if operator.gettokentype() == 'EQUAL':
                return Equal(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MORE':
                return Gthan(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'LESS':
                return Lthan(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'GEQUAL':
                return Gequal(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'LEQUAL':
                return Lequal(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'NOT_EQUAL':
                return Not_equal(self.builder, self.module, left, right)
            
        @self.pg.production('bool : bool AND bool')
        def and_bool(p):
            return And_(self.builder, self.module, p[0], p[2])
        
        @self.pg.production('bool : bool OR bool')
        def or_bool(p):
            return Or_(self.builder, self.module, p[0], p[2])
        
        @self.pg.production('bool : NOT bool')
        def not_bool(p):
            return Not_(self.builder, self.module, p[1])
        
        @self.pg.production('bool : OPEN_PAREN bool CLOSE_PAREN')
        def paren_bool(p):
            return p[1]
        
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expressoin(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)
        
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)
        
        @self.pg.production('expression : SUB NUMBER')
        def number(p):
            return Number(self.builder, self.module, str(0 - int(p[1].value)))
        
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def paren_expr(p):
            return p[1]

        @self.pg.production('expression : ID')
        def id_expr(p):
            return Load_(self.builder, self.module, p[0])
        
        @self.pg.production('expression : ID OPEN_PAREN ids CLOSE_PAREN')
        def function_expr(p):
            return Call_(self.builder, self.module, p[0], p[2])
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)
        
    def get_parser(self):
        return self.pg.build()