from string import digits
from typing import Generator

from myinterpreter.token_types import Token, TokenType


class Tokenizer:

    def __init__(self, code: str) -> None:
        self.code = code
        self.ptr: int= 0

    def __iter__(self) -> Generator[Token, None, None]:
        while (token := self.next_token()).type != TokenType.EOF:
            yield token
        yield token

    def next_token(self) -> Token:
        while self.ptr < len(self.code) and self.code[self.ptr] == " ":
            self.ptr += 1

        if self.ptr == len(self.code):
            return Token(TokenType.EOF)
        
        char = self.code[self.ptr]
        self.ptr += 1
        if char == "+":
            return Token(TokenType.PLUS)
        
        if char == "-":
            return Token(TokenType.MINUS)
        
        if char in digits:
            return Token(TokenType.INT, int(char))
        
        raise RuntimeError(f"Can't tokenize {char!r}")
    

