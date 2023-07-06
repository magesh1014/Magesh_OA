
# the sum of n terms of even natural numbers.
# Test Data :
# Input number of terms : 5
# Expected Output :
# The even numbers are :2 4 6 8 10
# The Sum of even Natural Number upto 5 terms : 30

n = int(input("Input number of terms :"))
even = []
sum = 0
for i in range(2,2*n+1,2):
    even.append(i)
    sum += i
print(f"The even numbers are : {even}")
print(f"The Sum of even Natural Number upto 5 terms : {sum}")