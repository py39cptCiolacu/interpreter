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


# --- Bytecode ---
class BytecodeType(StrEnum):
    PUSH = auto()
    BINOP = auto()
    UNARYOP = auto()


@dataclass
class Bytecode:
    type: BytecodeType
    value: Any


# -----Pratt Parsing-----
class AST:
    pass


@dataclass
class Int(AST):
    value: int


@dataclass
class UnaryOP(AST):
    op: TokenType
    operand: AST


@dataclass
class BinaryOp(AST):
    left: AST
    op: TokenType
    right: AST
