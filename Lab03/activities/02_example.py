# Implement a single regular expression for following numbers 8e4, 5e-2, 6e9

import re

pattern= r'^\-[0-9]+[Ee][+\-]?[0-9]'

input=input("Enter exponent number : ")

if re.match(pattern, input):
    print("The input is valid exponent expression : ",input)
else: 
    print("The input is not a valid exponenet expression : ",input )