import sys
from tokenizer import Tokenizer
from parser import Parser
from compiler import Compiler
from real_interpreter import Interpreter

def main():
    code = sys.argv[1]

    tokens = list(Tokenizer(code))
    tree = Parser(tokens).parse()
    bytecode = list(Compiler(tree).compile())
    Interpreter(bytecode).interpret()


if __name__ == "__main__":
    main()
