from string import digits
from typing import Generator

from interpreter_types import Token, TokenType

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

        match char:
            case "+":
                return Token(TokenType.PLUS)
        
            case "-":
                return Token(TokenType.MINUS)
        
            case "*":
                return Token(TokenType.MULTIPLY)
        
            case "/":
                return Token(TokenType.DIVIDE)
            

            # 123 + 587

            case c if c in digits:
                #OPTIMIZE THIS

                value = c
                for i in range(self.ptr, len(self.code)):
                    if self.code[i] not in digits:
                        self.ptr = i
                        return Token(TokenType.INT, value=int(value))
                    
                    value += self.code[i]

                self.ptr = len(self.code)
                return Token(TokenType.INT, value=int(value))

            
        raise RuntimeError(f"Can't tokenize {char!r}")
        
    

