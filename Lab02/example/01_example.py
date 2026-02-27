
import re

pattern = r'^[A-Za-z][0-9+=\-*/A-Za-z]{0,24}$'

regex = re.compile(pattern)

input=input("Enter input : ")

if re.match(pattern, input):
    print("Input belongs to pattern")
else: 
    print("Input does not belongs to pattern")