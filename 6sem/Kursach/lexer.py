from tkinter.tix import INTEGER
from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()
    
    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Types
        self.lexer.add('INTEGER', r'integer')
        self.lexer.add('FLOAT', r'float')
        # Functions
        self.lexer.add('FINCTION', r'function')
        # Begin End
        self.lexer.add('BEGIN', r'\{')
        self.lexer.add('END', r'\}')
        # If Else Then Do While
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('THEN', r'then')
        self.lexer.add('DO', r'do')
        self.lexer.add('WHILE', r'while')
        # ID
        self.lexer.add('ID', r'[a-zA-Z]*')
        # Break Continue
        self.lexer.add('BREAK', r'break')
        self.lexer.add('CONTINUE', r'continue')
        # Parent
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Binary operations
        self.lexer.add('AND', r'and')
        self.lexer.add('NOT', r'not')
        self.lexer.add('OR', r'or')
        self.lexer.add('NOT_EQUAL', r'\!=')
        self.lexer.add('EQUALS', r'\:=')
        # Operators
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('COLON', r'\:')
        self.lexer.add('COMMA', r'\,')
        self.lexer.add('EQUAL', r'\=')
        self.lexer.add('MORE', r'\>')
        self.lexer.add('LESS', r'\<')
        # Number
        self.lexer.add('NUMBER', r'[0-9]+(\.[0-9]+)?')
        # Ignore Spaces
        self.lexer.ignore(r'#[^\#]*#')
        self.lexer.ignore('\s+')
    
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
