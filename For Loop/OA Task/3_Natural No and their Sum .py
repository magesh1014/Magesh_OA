#  display n terms of natural numbers and their sum.
# Test Data : 7
# Expected Output :
# The first 7 natural number is :
# 1 2 3 4 5 6 7
# The Sum of Natural Number upto 7 terms : 28 

terms = int(input("How many terms to be printed: "))
sum=0
print(f"The first {terms} natural number is : ")
for i in range(1,terms+1):
    print(i, end=" ")
    sum += i
print()
print("The Sum is :", sum)
