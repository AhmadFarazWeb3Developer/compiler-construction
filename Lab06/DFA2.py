

state = 'q0'
input_string = input("Enter variable name: ")

for char in input_string:
    
    if state == 'q0':
        if char.isalpha() or char == '_': # islalpha() used for characters are letter or not 
            state = 'q1'
      
    elif state == 'q1':
        if char.isalnum() or char == '_': # isalnum() = letter OR digit an alpha numberic 
            state = 'q1'
            
    else:
            state = 'invalid'
            break

if state == 'q1':
    print("Accepted")
else:
    print("Rejected")

print(state)