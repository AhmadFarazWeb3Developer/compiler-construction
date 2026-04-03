state='q0'

input_string=input( "Enter input string: ")


for char in input_string:
      
      if state=='q0' and char=='a':
            state='q1'
      elif state=='q1' and char=='b':
            
            state = 'q1' 

      elif state=='q1' and char=='c':
            state='q2'
      elif state=='q2' and char=='d':
            state ='q3'
      else:
            state=='invalid'     
            break 

if state == 'q3':
 print("Accepted")
else:
 print("Rejected")

print(state)                   