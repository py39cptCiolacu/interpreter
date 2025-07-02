from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any

# --- Token-related ---
class TokenType(StrEnum):
    INT = auto()
    PLUS = auto()
    MINUS = auto()
    EOF = auto()

@dataclass
class Token:
    type: TokenType
    value: Any = None


# --- AST Tree ---
@dataclass
class TreeNode:
    pass

@dataclass
class BinOp(TreeNode):
    op: str
    left: int
    right: int

@dataclass
class Int(TreeNode):
    value: int


# --- Bytecode ---
class BytecodeType(StrEnum):
    PUSH = auto()
    BINOP = auto()

@dataclass
class Bytecode:
    type: BytecodeType
    value: Any
