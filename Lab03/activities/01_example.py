
# Implement a regular expression for floating point numbers having length not greater than 60.

import re

pattern= r'^[0-9]+\.[0-9]{0,59}$'


input=input("Enter floating number : ")

if re.match(pattern, input):
    print("Input belongs to pattern")
else: 
    print("Input does not belongs to pattern")