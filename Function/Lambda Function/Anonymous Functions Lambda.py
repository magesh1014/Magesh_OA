# lambda function is an anonymous function defined without a name and without using a def keyword

#  lambda function can take any number of arugument but can only have one expression

# syntax :
# lambda (arugument) : expression

# In normal functions
def addition(a,b):
    return a+b

print(addition(3,8))

# In Lambda function
add = lambda a,b: a+b
     #(argument):(expression)
print(add(3,8))
