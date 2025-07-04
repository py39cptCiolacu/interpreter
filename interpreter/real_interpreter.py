from stack import Stack
from interpreter_types import Bytecode, BytecodeType

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

                if bc.value not in ["+", "-", "*", "/"]:
                    raise RuntimeError(f"Unkown operator {bc.value}")
        
                left = self.stack.pop()

                match bc.value:
                    case "+":
                        result = left + right
                    case "-":
                        result = left - right
                    case "*":
                        result = left * right
                    case "/":
                        result = left / right
                        
                self.stack.push(result)

        print("Done!")
        print(self.stack)

