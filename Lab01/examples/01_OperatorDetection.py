# Simple program to check operators

operator=input("Enter a character: ")

if operator in '+-*/':
    print("The operator is arithmetic:",operator)
else:
    print("The operator is not arithmetic",operator)