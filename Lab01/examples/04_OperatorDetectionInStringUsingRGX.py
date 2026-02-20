# Simple program to check operator in a string using Regix or Regular expressions syntax
    
import re

text = input("Enter a string: ")

pattern = r'[+\-*/]'

if re.search(pattern, text):
    print("Arithmetic operator exists!")
else:
    print("No arithmetic operator found.")