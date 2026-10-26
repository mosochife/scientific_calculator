class CalculatorError(Exception):
    pass

def tokenize(text: str) -> list:
    # Raise error for empty input
    if not text:
        raise CalculatorError("Empty input")
    
    tokens = []
    i = 0
    while i < len(text):
        char = text[i]
        
        # Skip whitespace
        if char.isspace():
            i += 1
            continue
            
        # Numbers (including decimals)
        if char.isdigit() or char == '.':
            start = i
            while i < len(text) and (text[i].isdigit() or text[i] == '.'):
                i += 1
            tokens.append(text[start:i])
            continue
            
        # Names (letters)
        if char.isalpha():
            start = i
            while i < len(text) and text[i].isalpha():
                i += 1
            tokens.append(text[start:i])
            continue
            
        # Operators and parentheses
        if char in '+-*/^!()':
            tokens.append(char)
            i += 1
            continue
            
        # Unknown character
        raise CalculatorError(f"Unknown character: {char}")
        
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected=None):
        token = self.peek()
        if token is None:
            raise CalculatorError("Unexpected end of expression")
        if expected and token != expected:
            raise CalculatorError(f"Expected {expected}, got {token}")
        self.pos += 1
        return token

    def parse_expression(self):
        # Handles + and - (lowest precedence)
        left = self.parse_term()
        while self.peek() in ('+', '-'):
            op = self.consume()
            right = self.parse_term()
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left

    def parse_term(self):
        # Handles * and /
        left = self.parse_unary()
        while self.peek() in ('*', '/'):
            op = self.consume()
            right = self.parse_unary()
            if op == '*':
                left = left * right
            else:
                if right == 0:
                    raise CalculatorError("Division by zero")
                left = left / right
        return left

    def parse_unary(self):
        # Handles unary minus
        if self.peek() == '-':
            self.consume()
            return -self.parse_unary()
        return self.parse_power()

    def parse_power(self):
        # Handles ^ (right-associative)
        base = self.parse_primary()
        if self.peek() == '^':
            self.consume()
            exponent = self.parse_unary()
            return base ** exponent
        return base

    def parse_primary(self):
        # Handles numbers and parentheses
        token = self.peek()
        if token is None:
            raise CalculatorError("Unexpected end of expression")
        
        if token == '(':
            self.consume('(')
            value = self.parse_expression()
            self.consume(')')
            return value
        
        if token.replace('.', '', 1).isdigit():
            self.consume()
            return float(token)
            
        raise CalculatorError(f"Unexpected token: {token}")

def evaluate(expression, angle_mode="deg"):
    tokens = tokenize(expression)
    parser = Parser(tokens)
    result = parser.parse_expression()
    
    # Check for leftover tokens
    if parser.peek() is not None:
        raise CalculatorError(f"Unexpected token after expression: {parser.peek()}")
        
    return result
