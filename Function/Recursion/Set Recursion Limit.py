import sys

sys.setrecursionlimit(1986)
print(sys.getrecursionlimit())

i = 0

def greet():
    global i 
    i+=1
    print("hello", i)
    greet()
    
greet()