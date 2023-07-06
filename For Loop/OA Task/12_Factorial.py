
# calculate the factorial of a given number.
# Test Data :
# Input the number : 5
# Expected Output :
# The Factorial of 5 is: 120

num = int(input("Input the number : "))
fact = 1
for i in range(1,num+1):
    fact*=i
print(f"The Factorial of 5 is : {fact}")