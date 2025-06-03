import time
value1=int(input("Enter value1:\n"))
value2=int(input("Enter value2:\n"))
while(True):
 try:
  answer=value1/value2
 
 except:
    print("The input entered are not valid. Please enter correct input")
    value1=int(input("Enter value1:\n"))
    value2=int(input("Enter value2:\n"))
    
 
 else:
    print('Great!, correct input values.\n Processing your input')
    time.sleep(3)
    print('Answer is:')
    print(answer)
    break
 
 finally:
     print('DONE')
     exit
   
    