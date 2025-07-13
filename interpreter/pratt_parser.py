from interpreter_types import (
    Token,
    TokenType,
    AST,
    Int,
    UnaryOP,
    BinaryOp,
    Assignment,
    Variable,
)

PRECEDENCE = {
    TokenType.PLUS: 10,
    TokenType.MINUS: 10,
    TokenType.MULTIPLY: 20,
    TokenType.DIVIDE: 20,
}


class PrattParser:

    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.pos: int = 0
        self.current = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current = self.tokens[self.pos]
        else:
            self.current = Token(TokenType.EOF)

    def parse(self):
        return self.expression(0)

    def expression(self, rbp: int):
        t = self.current
        self.advance()
        left = self.nud(t)

        while rbp < self.lbp(self.current):
            t = self.current
            self.advance()
            left = self.led(t, left)

        return left

    def lbp(self, token: Token):
        return PRECEDENCE.get(token.type, 0)

    def nud(self, token: Token):
        if token.type == TokenType.INT:
            return Int(value=token.value)

        elif token.type == TokenType.IDENTIFIER:
            name = token.value
            if self.current.type == TokenType.EQUAL:
                self.advance()
                expr = self.expression(0)
                return Assignment(name, expr)
            else:
                return Variable(name)

        elif token.type == TokenType.MINUS:
            return UnaryOP(op=token.type, operand=self.expression(100))

        raise SyntaxError(f"Unexpected token (nud): {token}")

    def led(self, token: Token, left):
        right = self.expression(self.lbp(token))
        return BinaryOp(left=left, op=token.type, right=right)
