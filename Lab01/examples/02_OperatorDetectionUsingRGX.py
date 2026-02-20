# Simple program to check operator as input using Regix or Regular expressions syntax

import re

char=input("Enter a character: ")

pattern=r'^[+\-*/]$' # minus has a special meaning thats why \ helps to make the difference 

if  re.match(pattern,char) :
    print("The operator is arithmetic:")
else:
    print("The operator is not arithmetic")