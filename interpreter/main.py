from pprint import pprint
from tokenizer import Tokenizer
from parser import Parser
from compiler import Compiler
from real_interpreter import Interpreter

def main():
    #code = sys.argv[1]

    code = "3 * 5 + 5 * 8 + 1 - 2"

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

        
    tokens = list(Tokenizer(code))
    
    tree_new = Parser(tokens).new_parse()
    pprint(tree_new)

    # tree = Parser(tokens).parse()
    # bytecode = list(Compiler(tree).compile())
    # Interpreter(bytecode).interpret()


if __name__ == "__main__":
    main()
