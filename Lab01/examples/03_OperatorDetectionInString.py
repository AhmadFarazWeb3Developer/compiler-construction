# Simple program to check operator as input using Regix or Regular expressions syntax

str=input("Enter a string: ")

pattern=['+','-','/','*']

for operator in pattern:
    if operator in str:
        print("Arithmetic operator exists!")
         