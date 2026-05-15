import re

symbol_table = {}

def tokenize(code):
    tokens = re.findall(r'\w+|[=+*()-]', code)
    print("Tokens Generated Successfully")
    return tokens

def syntax_check(expr):
    pattern = r'^[a-zA-Z_]\w*\s*=\s*(\d+)(\s*[\+\*]\s*(\d+))*$'
    return re.match(pattern, expr)

def optimize(expr):
    var, value = expr.split("=")
    result = eval(value)
    return result

def mini_compiler(code):
    # Step 1: Tokenization
    tokenize(code)

    # Step 2: Syntax Check
    if syntax_check(code):
        print("Syntax Valid")
    else:
        print("Syntax Error")
        return

    # Step 3: Optimization
    result = optimize(code)

    print("Optimized Result =", result)

# Test
code = "result = 5 + 3 * 2"
mini_compiler(code)