# find the 'Perfect' numbers within a given number of ranges.
# Test Data :
# Input the starting range or number : 1
# Input the ending range of number : 50
# Expected Output :
# The Perfect numbers within the given range : 6 28
        
s = int(input("Input the starting range of number : "))
e = int(input("Input the ending range of number : "))
perfectnum = []
for i in range(s,e+1):
    divisor = []
    for j in range(s,i):
        if i%j==0:
            divisor.append(j)
    if i == sum(divisor):
        perfectnum.append(i)
print(f"The Perfect numbers within the given range : {perfectnum}")