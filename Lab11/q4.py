def constant_folding(expr):
    var, value = expr.split("=")
    result = eval(value)
    return f"{var.strip()} = {result}"

# Test
expr = "x = 2 + 3 * 4"
print(constant_folding(expr))