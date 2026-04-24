input_tokens = [
    "int","ID","=","NUM",";",
    "int","ID","=","NUM",";",
    "int","ID","=","NUM",";",
    "ID","=","ID","+","ID",";",
    "if","(","ID",">","NUM",")",
    "print","ID",";",
    "else",
    "print","ID",";"
]

def parse(tokens):
    stack = []
    i = 0

    while i < len(tokens):
        # SHIFT
        stack.append(tokens[i])
        i += 1

        # DECL
        while len(stack) >= 5 and stack[-5:] == ["int","ID","=","NUM",";"]:
            stack = stack[:-5]
            stack.append("DECL")

        #  ASSIGN
        while len(stack) >= 6 and stack[-6:] == ["ID","=","ID","+","ID",";"]:
            stack = stack[:-6]
            stack.append("ASSIGN")

        #  PRINT
        while len(stack) >= 3 and stack[-3:] == ["print","ID",";"]:
            stack = stack[:-3]
            stack.append("PRINT")

        #  CONDITION
        while len(stack) >= 3 and stack[-3:] == ["ID",">","NUM"]:
            stack = stack[:-3]
            stack.append("COND")

        #  IF-ELSE → IFSTMT
        while len(stack) >= 6 and stack[-6:] == ["if","(","COND",")","PRINT","else"]:
            stack = stack[:-6]
            stack.append("IFSTMT")

    print("Final Stack:", stack)


parse(input_tokens)