# displays the n terms of square natural numbers and their sum.
# 1 4 9 16 ... n Terms
# Test Data :
# Input the number of terms : 5
# Expected Output :
# The square natural upto 5 terms are :1 4 9 16 25
# The Sum of Square Natural Number upto 5 terms = 55

n = int(input("Input the number of terms :"))
sum = 0
sq = []
for i in range(1,n+1):
    power = i**2
    sq.append(power)
    sum += power
print(f"\nThe square natural upto {n} terms are : {sq} ")
print(f"The Sum of Square Natural Number upto {n} terms = {sum}")