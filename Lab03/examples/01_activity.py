import re


pattern= r'^(if|else|void|main|int|for|while|break|continue)'

input = input("Enter any string : ")

if re.match(pattern, input):
    print("Keyword detected") 
else:
    print("No keyword detected")
    
