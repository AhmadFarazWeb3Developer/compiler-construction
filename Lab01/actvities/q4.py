import re

input = input("Enter input:")

pattern = r'\s+'

new_string=re.sub(pattern, "", input)

print(new_string)