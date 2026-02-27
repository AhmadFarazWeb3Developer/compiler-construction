import re

pattern = r'^[A-Za-z][A-Za-z0-9]{5,11}$'

password = input("Enter a valid password :")

if re.match(pattern,password):
    print("Password belongs to pattern")
    
else:    
    print("Password does'nt belongs to pattern")
