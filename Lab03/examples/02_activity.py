import re

pattern= r'^-?[0-9]+(\.[0-9])?([Ee][-+]?[0-9])?$'


input = input("Enter any string : ")

if re.match(pattern, input):
    print("Belongs to pattern",input) 
else:
    print("Do not belongs to pattern")
    
