from pprint import pprint
import sys

from tokenizer import Tokenizer
from pratt_parser import PrattParser
from compiler import Compiler
from real_interpreter import Interpreter


def main():
    code = sys.argv[1]

    # code = "3 + 5 * 5 + 2 + 9 - 1 * 12 + 2 - 1"

    # left = 3
    # op = +
    # right =
    #     left =
    #         left = 5
    #         op = *
    #         right =
    #             left = 5
    #             op = *
    #             right = 8
    #     op = +
    #     right =
    #         left = 1
    #         op = -
    #         right  2

    # 1. From STR to TOKENS-LIST
    tokens = list(Tokenizer(code))

    # 2. From TOKENS-LIST to AST
    parser = PrattParser(tokens)
    ast = parser.parse()
    pprint(ast)

    # 3. From AST to BYTECODE-LIST
    compiler = Compiler(ast)
    bytecode = compiler.compile()
    pprint(bytecode)

    # 4. From BYTECODE-LIST to RESULT
    Interpreter(bytecode).interpret()


if __name__ == "__main__":
    main()
