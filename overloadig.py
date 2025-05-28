
from multipledispatch import dispatch

@dispatch(int,int)
def subtract(a, b):
        print(a-b)
        
@dispatch(int,int,int)
        
def subtract(a, b,c):
        print(a-b-c)
         
subtract(2,3)
subtract(2,3,4)
