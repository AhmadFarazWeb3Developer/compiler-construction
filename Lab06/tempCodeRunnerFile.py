state='q0'

input_string="aabbbbbbbbcd"


for char in input_string:
      if state=='q0' and char=='a':
            state='q1'
            print('hit1')
      elif state=='q1' or char=='b':
            state='q2'
            print('hit2')
      elif state=='q2' and char=='c':
            state='q3'
            print('hit3')
      elif state=='q3' and char=='d':
            state ='q4'
            print('hit4')

      else:
            state=='invalid'     
            break 

if state == 'q4':
 print("Accepted")
else:
 print("Rejected")

print(state)                   