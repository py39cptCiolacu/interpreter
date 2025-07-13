from interpreter_types import (
    Bytecode,
    BytecodeType,
    AST,
    Token,
    Int,
    UnaryOP,
    BinaryOp,
    Variable,
    Assignment,
)


class Compiler:
    def __init__(self, tree: AST) -> None:
        self.tree = tree

    def compile(self) -> list[Bytecode]:
        return self._compile_node(self.tree)

    def _compile_node(self, node: AST) -> list[Bytecode]:
        match node:

            case Int(value=value):
                return [Bytecode(BytecodeType.PUSH, value)]

            case Variable(name=name):
                return [Bytecode(BytecodeType.LOAD, name)]

            case Assignment(name=name, value=value):
                return self._compile_node(value) + [Bytecode(BytecodeType.STORE, name)]

            case UnaryOP(op=op, operand=operand):
                return self._compile_node(operand) + [
                    Bytecode(BytecodeType.UNARYOP, op)
                ]

            case BinaryOp(left=left, op=op, right=right):
                return (
                    self._compile_node(left)
                    + self._compile_node(right)
                    + [Bytecode(BytecodeType.BINOP, op)]
                )

        raise TypeError(f"Unkown AST node: {node}")
