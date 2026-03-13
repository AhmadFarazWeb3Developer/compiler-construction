# Write a Python program that reads a line of code in a single buffer and prints all keywords in the code.

keywords = ["int", "float", "if", "else", "while", "return"]

operators = ["+", "-", "*", "/", "=", "==", "<", ">", "<=", ">="]

separators = [";", ",", "(", ")", "{", "}"]

source_code="int a = 10 ; float b ; if a > b return a ;"


buffer_size = 8

def lexical_analyzer(source_code):
  
    tokens = [] 
   # 'i' starts at 0 → first buffer is source_code[0:8]
   # next iteration, 'i' = 8 → next buffer is source_code[8:16]
   # then 'i' = 16 → next buffer is source_code[16:24], and so on

    for i in range(0, len(source_code), buffer_size):
        
     buffer = source_code[i:i+buffer_size]
     
     words = buffer.split()
     
     for word in words:
      if word in keywords:
        tokens.append(("KEYWORD", word))
      elif word in operators:
        tokens.append(("OPERATOR", word))
      elif word in separators:
        tokens.append(("SEPARATOR", word))
      else:
        tokens.append(("IDENTIFIER", word))

    return tokens



result = lexical_analyzer(source_code)

print(result)
