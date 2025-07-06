from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Union

# --- Token-related ---
class TokenType(StrEnum):
    INT = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
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
class AST:
    op: str
    left: Union[int, BinOp, AST]
    right: Union[int, BinOp, AST]

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
