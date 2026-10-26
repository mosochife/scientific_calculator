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
