from dataclasses import dataclass

from interpreter_types import Token, TokenType, BinOp, Int, AST

class Parser:

    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.next_token_index: int = 0
        # self.next_token_index: int = 0 => not 0, but start index of subtree
        # self.last_token_index: int 
        
    def eat(self, expected_token_type: TokenType) -> Token:
        """Returns the next token if it is of the expected type.
        If the next token is not of the expected type, this raises an error.
        """

        next_token = self.tokens[self.next_token_index]
        self.next_token_index += 1

        if next_token.type != expected_token_type:
            raise RuntimeError(f"Expected {expected_token_type}, ate {next_token!r}")
        
        return next_token
    

    def peek(self, skip: int = 0) -> TokenType | None:
        """Checks the type of an upcoming token without consuming it."""

        peek_at = self.next_token_index + skip

        if peek_at > len(self.tokens):
            return None
        
        return self.tokens[peek_at].type
        
    def peek_and_eat_op(self) -> str:
        match self.peek():
            case TokenType.PLUS:
                op = "+"
                self.eat(TokenType.PLUS)

            case TokenType.MINUS:
                op = "-"
                self.eat(TokenType.MINUS)

            case TokenType.MULTIPLY:
                op = "*"
                self.eat(TokenType.MULTIPLY)

            case TokenType.DIVIDE:
                op = "/"
                self.eat(TokenType.DIVIDE)

            case _ :
                print(self.peek())
                raise RuntimeError("Given operation is not accepted!")
            
        return op
    
    def new_parse(self) -> AST:
        inital_root_index = self.find_root_in_future_ast(0, len(self.tokens))
        left = self.create_AST(0, inital_root_index)
        op = self.peek_and_eat_op()
        right= self.create_AST(inital_root_index+1, len(self.tokens)-1)

        return AST(op=op, left=left, right=right)
    
    def find_root_in_future_ast(self, start: int, end: int) -> int:
        """
        this code return the index of the first + or - TOKEN find in the given interval
        if there is not + or - start+1 is returned
        """
        curr_skip = 1 
        while True:
            if self.peek(curr_skip) in [TokenType.MINUS, TokenType.PLUS]:
                return curr_skip + start
            
            curr_skip += 2
            if curr_skip+start >= end:
                # and root_index will be the initial root_index passes in function => start + 1
                break        

        
        return start+1
    
    def create_AST(self, start, end):
        """
        check if end-start == 1 -> last item (i guess)
        check if - end - start == 3 => AST == BinOP  :: 3 + 5 
        calculate root_index
        if len(left) == 1 => append to AST as int
        if len(left) > 1 => call recursive create_AST
        same for right
        """
        if end-start == 1:
            return self.eat(TokenType.INT)
        
        if end-start == 3:
            left = self.eat(TokenType.INT)
            op = self.peek_and_eat_op()
            right = self.eat(TokenType.INT)
            return AST(op=op, left=left, right=right)
        
        ast_root_index = self.find_root_in_future_ast(start, end)

        if ast_root_index - start == 1:
            left = self.eat(TokenType.INT)
        else:
            left = self.create_AST(start, ast_root_index-1)

        print("Trying to eat ", self.peek())
        op = self.peek_and_eat_op()
        
        if end - ast_root_index == 1:
            right = self.eat(TokenType.INT)
        else:
            right = self.create_AST(ast_root_index+1, end)

        return AST(op=op, left=left, right=right)
                
    # def __create_BinOP(self):
    #     left = self.eat(TokenType.INT)
    #     print("Trying to eat ", self.peek())
    #     op = self.peek_and_eat_op()
    #     right = self.eat(TokenType.INT)

    #     return BinOp(op=op, left=left, right=right)

    def parse(self) -> BinOp:
        left_op = self.eat(TokenType.INT)

        match self.peek():
            case TokenType.PLUS:
                op = "+"
                self.eat(TokenType.PLUS)

            case TokenType.MINUS:
                op = "-"
                self.eat(TokenType.MINUS)

            case TokenType.MULTIPLY:
                op = "*"
                self.eat(TokenType.MULTIPLY)

            case TokenType.DIVIDE:
                op = "/"
                self.eat(TokenType.DIVIDE)

        right_op = self.eat(TokenType.INT)

        return BinOp(op, int(left_op.value), int(right_op.value))
    