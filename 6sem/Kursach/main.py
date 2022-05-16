import code
from pygments import lex
from lexer import Lexer
from parser import Parser
from codegen import CodeGen

fname = 'input.my'

with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
new_tokens = lexer.lex(text_input)

token_stream = []
for t in new_tokens:
    token_stream.append(t)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf, struct)
pg.parse()
parser = pg.get_parser
parse = parser.parse(tokens)
parse.eval()

codegen.create_ir()
codegen.save_ir(output.ll)