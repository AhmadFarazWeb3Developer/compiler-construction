symbol_table = {}

def evaluate(expr):
    try:
        return eval(expr, {}, symbol_table)
    except:
        return None

def process_code(lines):
    for line in lines:
        parts = line.split()

        if parts[0] == "int":
            var = parts[1]
            symbol_table[var] = 0

        elif "=" in line:
            var, expr = line.split("=")
            var = var.strip()
            expr = expr.strip()
            value = evaluate(expr)
            symbol_table[var] = value

    print("\nSymbol Table")
    print("Variable\tType\tValue")
    for var in symbol_table:
        print(f"{var}\t\tint\t{symbol_table[var]}")

# Test
lines = [
    "int a",
    "int b",
    "a = 10",
    "b = a + 5"
]

process_code(lines)