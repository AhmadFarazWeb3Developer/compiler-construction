import re

input= input("Input a char: ")
pattern=r'^(and|or|not)$' # () brackets are used for group of character and [] used for characters

if re.match(pattern,input):
    print("Logical operator exists!")
else:
    print("No logical operator found.")



