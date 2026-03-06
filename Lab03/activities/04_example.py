# Implement a regex in Python to detect valid email addresses in a string.
#   Requirements:
#     1. An email consists of:
#       o A username: letters, digits, dots (.), underscores (_), or hyphens (-)
#       o The @ symbol
#       o A domain name: letters, digits, dots (.), or hyphens (-)
#       o A top-level domain (TLD): letters only (2–6 characters, like .com, .org, .edu)

import re

pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$'

input=input("Enter an email : ")

if re.match(pattern, input):
    print("The email is valid : ",input)
else: 
    print("The email is invalid: ",input )
    
    