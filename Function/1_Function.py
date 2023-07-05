#  a function is a set of instruction to perform a specific task

# python functions :

def multiply():
# def = keyword that means "define"
# multiply = function name
    a = 2       # function body
    b = 3       # a and b were created inside the function
    return a*b
# return represent end of the function 
# [a*b] = must output some kind of data type {432,false,"string",[1,2,3]}
# in absence of data, return statement can be skip by replacing print statement
    
    print(hello)

# only defining the function is not enough, we also need to call it
multiply()      #call function

if "a">"b":         # a and b don't exist outside the function
    print("a")

# # # NameError : name "a" is not defined

def multiply(a,b):  #(a,b) are known as parameter these are placeholder for arguments
    print(a*b)
    
multiply(2,4)       #(2,4) are known as arguments to assign value to parameters
multiply(3,4)
 