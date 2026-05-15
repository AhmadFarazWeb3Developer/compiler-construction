import re

keywords = {"int", "float", "if", "else", "while", "return"}

def lexical_analyzer(code):
    tokens = re.findall(r'\w+|[=+*()-]', code)

    for token in tokens:
        if token in keywords:
            print("KEYWORD :", token)
        elif token.isidentifier():
            print("IDENTIFIER :", token)
        elif token.isdigit():
            print("NUMBER :", token)
        elif token in "+-*/=":
            print("OPERATOR :", token)
        else:
            print("SYMBOL :", token)

# Test
code = "a = 10 + 20"
lexical_analyzer(code)