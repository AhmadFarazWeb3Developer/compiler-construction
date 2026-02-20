
import re

text= input("Enter input: ")
pattern=['if','else','for','int','float','while','<','>','==','!=','<=','>=','and','or','not']

for keyword in pattern:
    if(keyword in text):
        print(f"System defined \"{keyword}\" keyword exists!")

