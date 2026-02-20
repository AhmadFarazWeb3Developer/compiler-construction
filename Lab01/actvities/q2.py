
import re

input= input("Input a char: ")
pattern=r'^(<|>|==|!=|<=|>=)$'

if re.match(pattern,input):
    print("Relational operator exists!")
else:
    print("No Relational operator found.")


