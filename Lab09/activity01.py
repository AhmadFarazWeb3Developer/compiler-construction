
import re

def lexical_analysis(expr):
    
    tokens = []
    parts = expr.split()

    parts = re.findall(r'\d+|\+', expr) # Use regex to find numbers 0-9 or operators. 

    for part in parts:
        if part.isdigit():
            tokens.append(("NUMBER", part)) #append a tuple (type, value)
        elif part == "+":
            tokens.append(("OPERATOR", part))
        else:
            tokens.append(("INVALID", part))

    return tokens


def syntax_analysis(tokens):
    if len(tokens) != 3:
        return False

    if (
        tokens[0][0] == "NUMBER" and
        tokens[1] == ("OPERATOR", "+") and
        tokens[2][0] == "NUMBER"
    ):
        return True

    return False


def evaluate(tokens):
    return int(tokens[0][1]) + int(tokens[2][1])  


# Main
expr = input("Enter expression: ")

tokens = lexical_analysis(expr)
print("Tokens:", tokens)

if syntax_analysis(tokens):
    print("Valid syntax")
    print("Result =", evaluate(tokens))
else:
    print("Invalid syntax")