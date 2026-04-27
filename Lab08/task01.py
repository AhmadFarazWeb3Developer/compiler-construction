import re

# Token patterns
token_specification = [
    ('KEYWORD',   r'\b(int|float|char)\b'),
    ('IDENTIFIER',r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('NUMBER',    r'\b\d+\b'),
    ('OPERATOR',  r'[=+\-*/]'),
    ('DELIMITER', r'[;,]'),
    ('SKIP',      r'[ \t\n]+'),
    ('MISMATCH',  r'.')
]

# Combine regex
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

# Symbol table
symbol_table = {}
memory_address = 1000

def lexical_analyzer(code):
    tokens = []
    global memory_address

    current_type = None

    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind == 'KEYWORD':
            current_type = value
            tokens.append((kind, value))

        elif kind == 'IDENTIFIER':
            tokens.append((kind, value))

            # Add to symbol table if declaration
            if current_type:
                if value not in symbol_table:
                    symbol_table[value] = {
                        'type': current_type,
                        'memory': memory_address,
                        'value': None
                    }
                    memory_address += 4

        elif kind == 'NUMBER':
            tokens.append((kind, value))

        elif kind == 'OPERATOR':
            tokens.append((kind, value))

        elif kind == 'DELIMITER':
            tokens.append((kind, value))

            # Reset type after ';'
            if value == ';':
                current_type = None

        elif kind == 'SKIP':
            continue

        elif kind == 'MISMATCH':
            print(f"Unexpected character: {value}")

    return tokens


def handle_assignments(code):
    assignments = re.findall(r'(\b[a-zA-Z_]\w*\b)\s*=\s*(\d+)', code)

    for var, val in assignments:
        if var in symbol_table:
            symbol_table[var]['value'] = int(val)


# ----------- MAIN -----------

code = """
int a, b;
float x;
a = 10;
b=20;
x = 5;
"""

tokens = lexical_analyzer(code)
handle_assignments(code)

# Display Tokens
print("Tokens:")
for t in tokens:
    print(t)

# Display Symbol Table
print("\nSymbol Table:")
print("Name\tType\tMemory\tValue")

for name, info in symbol_table.items():
    print(f"{name}\t{info['type']}\t{info['memory']}\t{info['value']}")