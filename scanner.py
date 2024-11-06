import re  # Import the regular expressions library

# Define regex patterns for various Python tokens
TOKEN_PATTERNS = {
    'KEYWORD': r'\b(False|None|True|and|as|assert|async|await|break|class|continue|'
               r'def|del|elif|else|except|finally|for|from|global|if|import|in|is|'
               r'lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b',
    # Matches Python keywords using word boundaries to ensure full word matches
    
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    # Matches identifiers that start with a letter or underscore, followed by letters, digits, or underscores
    
    'NUMBER': r'\b\d+(\.\d+)?\b',
    # Matches integers and floats, e.g., 123, 45.67
    
    'OPERATOR': r'==|!=|<=|>=|<|>|\+|\-|\*|\/|\/\/|\%|\*\*|\=|\+=|\-=|\*=|\/=|\/\/=|\%=|\*\*=',
    # Matches various Python operators, including arithmetic, comparison, and assignment operators
    
    'DELIMITER': r'[;,\(\)\{\}\[\]\:]',
    # Matches common delimiters, such as parentheses, braces, brackets, colons, commas, and semicolons
    
    'STRING': r'(\".*?\"|\'.*?\')',
    # Matches single-line string literals enclosed in double or single quotes
    
    'WHITESPACE': r'\s+',
    # Matches whitespace, including spaces, tabs, and newlines (used to ignore in tokenization)
    
    'UNKNOWN': r'.'
    # Matches any unrecognized character, allowing us to handle unexpected input gracefully
}

# Compile all regex patterns into a single regex object with named groups for each token type
TOKEN_REGEX = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_PATTERNS.items()))

def scanner(input_text):
    """A scanner that tokenizes Python-like input text."""
    position = 0  # Position in the input text
    tokens = []   # List to store the generated tokens

    # Process input text until we reach the end
    while position < len(input_text):
        # Attempt to match a token pattern at the current position
        match = TOKEN_REGEX.match(input_text, position)
        
        if match:
            # Retrieve the token type (matched regex group name) and its value (matched text)
            token_type = match.lastgroup
            token_value = match.group(token_type)

            # Skip whitespace tokens as they are not needed in further analysis
            if token_type != 'WHITESPACE':
                tokens.append((token_type, token_value))
            
            # Move the current position to the end of the matched token
            position = match.end()
        else:
            # Raise an error if no valid token matches the current input position
            raise SyntaxError(f"Unknown token at position {position}")
    
    return tokens  # Return the list of identified tokens

# Example usage with some Python code
input_code = """
def calculate_sum(x, y):
    if x > y:
        return x - y
    else:
        return x + y
"""
tokens = scanner(input_code)

# Print each token in the generated list
for token in tokens:
    print(token)
