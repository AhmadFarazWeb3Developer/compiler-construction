keywords = ["int", "float", "if", "else", "while", "return"]
operators = ["+", "-", "*", "/", "=", "==", "<", ">", "<=", ">="]
separators = [";", ",", "(", ")", "{", "}"]

buffer_size = 8

def lexical_analyzer(source_code):

    tokens = []

    buffer1 = ""
    buffer2 = ""
    words = ""

    i = 0
    n = len(source_code)

    while i < n:

        buffer1 = source_code[i:i+buffer_size]
        i += buffer_size
        words += buffer1

        if i >= n:
            break

        buffer2 = source_code[i:i+buffer_size]
        i += buffer_size
        words += buffer2

    words = words.split()

    for word in words:
        if word in keywords:
            tokens.append(("KEYWORD", word))
        elif word in operators:
            tokens.append(("OPERATOR", word))
        elif word in separators:
            tokens.append(("SEPARATOR", word))
        elif word.isdigit():
            tokens.append(("NUMBER", word))
        else:
            tokens.append(("IDENTIFIER", word))

    return tokens


source_code = "int a = 10 ; float b = 20 ; if a > b return a ;"

result = lexical_analyzer(source_code)
print(result)