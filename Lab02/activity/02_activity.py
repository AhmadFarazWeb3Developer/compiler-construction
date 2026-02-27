import re

pattern = r'^[aAeEiIoOuU][A-Za-z]{2,}\b' 
paragraph= input("Enter any string: ").split()

words=[] 

for word in paragraph:
    if re.match (pattern,word):
        words.append(word)
        
print(words)


