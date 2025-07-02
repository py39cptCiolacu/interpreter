from compiler import Bytecode, BytecodeType
from stack import Stack

class Interpreter:

    def __init__(self, bytecode: list[Bytecode]) -> None:
        self.stack = Stack()
        self.bytecode = bytecode
        self.ptr: int = 0

    def interpret(self) -> None:
        for bc in self.bytecode:
            if bc.type == BytecodeType.PUSH:
                self.stack.push(bc.value)
            elif bc.type == BytecodeType.BINOP:
                right = self.stack.pop()
                left = self.stack.pop()
                if bc.value == "+":
                    result = left + right
                elif bc.value == "-":
                    result = left - right
                else:
                    raise RuntimeError(f"Unkown operator {bc.value}")
                
                self.stack.push(result)

        print("Done!")
        print(self.stack)

if __name__ == "__main__":
    import sys

    from tokenizer import Tokenizer
    from parser import Parser
    from compiler import Compiler

    # code = sys.argv[1]

    code = "3 + 7 + 1"
    tokens = list(Tokenizer(code))
    tree = Parser(tokens).parse()
    bytecode = list(Compiler(tree).compile())
    Interpreter(bytecode).interpret()
