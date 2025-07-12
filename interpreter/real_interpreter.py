from stack import Stack
from interpreter_types import Bytecode, BytecodeType
from pprint import pprint


class Interpreter:

    def __init__(self, bytecode: list[Bytecode]) -> None:
        self.stack = Stack()
        self.bytecode = bytecode
        self.ptr: int = 0

    def interpret(self) -> None:
        pprint(self.bytecode)

        for bc in self.bytecode:
            if bc.type == BytecodeType.PUSH:
                self.stack.push(bc.value)
                print(f"PUSH: {bc.value}")
            elif bc.type == BytecodeType.BINOP:
                right = self.stack.pop()
                print(f"POP: {right}")

                if bc.value not in ["plus", "minus", "multiply", "divide"]:
                    raise RuntimeError(f"Unkown operator {bc.value}")

                left = self.stack.pop()
                print(f"POP: {left}")

                match bc.value:
                    case "plus":
                        result = left + right
                    case "minus":
                        result = left - right
                    case "multiply":
                        result = left * right
                    case "divide":
                        result = left / right

                self.stack.push(result)
                # print(f"PUSH: {result}")

        print("Done!")
        print(self.stack)
