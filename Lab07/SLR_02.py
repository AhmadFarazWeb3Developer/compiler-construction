stack = []

tokens = [
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
        token = tokens[i]
        stack.append(token)
    

        #  DECL
        if len(stack) >= 5 and stack[-5:] == ["int","ID","=","NUM",";"]:
            stack = stack[:-5]
            stack.append("DECL")
            

        #  ASSIGN
        elif len(stack) >= 6 and stack[-6:] == ["ID","=","ID","+","ID",";"]:
            stack = stack[:-6] # remove last 6 tokens and replace with ASSIGN
            stack.append("ASSIGN")

        #  PRINT
        elif len(stack) >= 3 and stack[-3:] == ["print","ID",";"]:
            stack = stack[:-3]
            stack.append("PRINT")
           

        #  CONDITION
        elif len(stack) >= 3 and stack[-3:] == ["ID",">","NUM"]:
            stack = stack[:-3]
            stack.append("COND")


        
        elif len(stack) >= 6 and stack[-6:] == ["if","(","COND",")","PRINT","else"]:
            stack = stack[:-6]
            stack.append("IF_PART")
       

        #  IF ELSE COMPLETE
        elif len(stack) >= 2 and stack[-2:] == ["IF_PART","PRINT"]:
            stack = stack[:-2]
            stack.append("IFSTMT")
    


        i += 1

    print("Final Stack:", stack)


parse(tokens)