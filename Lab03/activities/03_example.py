# Implement a regex in Python to detect valid hexadecimal numbers in a string 0x12345678

import re

pattern=r'0[xX][0-9A-Fa-f]+'

text = input("Enter input string: ")

if re.search(pattern, text):
    print("Hexadecimal detected in the string")
else:
    print("No hexadecimal in the string")
   