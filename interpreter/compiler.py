from typing import Generator

from interpreter_types import BinOp, Bytecode, BytecodeType

class Compiler:

    def __init__(self, tree: BinOp) -> None:
        self.tree = tree

    def compile(self) -> Generator[Bytecode, None, None]:
        left = self.tree.left

        yield Bytecode(BytecodeType.PUSH, left)

        right = self.tree.right

        yield Bytecode(BytecodeType.PUSH, right)

        yield Bytecode(BytecodeType.BINOP, self.tree.op)