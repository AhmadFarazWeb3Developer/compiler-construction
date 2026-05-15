import re

def is_valid_expression(expr):
    pattern = r'^[a-zA-Z_]\w*\s*=\s*(\d+|[a-zA-Z_]\w*)(\s*[\+\*]\s*(\d+|[a-zA-Z_]\w*))*$'
    return re.match(pattern, expr)

# Test
expr = "x = 5 + 2 * 4"

if is_valid_expression(expr):
    print("Valid Expression")
else:
    print("Invalid Expression")