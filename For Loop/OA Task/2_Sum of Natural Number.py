# sum of the first 10 natural numbers.
# Expected Output :
# The first 10 natural number is :
# 1 2 3 4 5 6 7 8 9 10
# The Sum is : 55

sum=0
print("The first 10 natural number is : ")
for i in range(1,11):
    print(i, end=" ")
    sum += i
print()
print("The Sum is :", sum)