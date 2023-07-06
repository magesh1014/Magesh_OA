# find the sum of the series 1 +11 + 111 + 1111 + .. n terms.
# Test Data :
# Input the number of terms : 5
# Expected Output :
# 1 + 11 + 111 + 1111 + 11111
# The Sum is : 12345

n = int(input("Input the number of terms : "))
num = 1
sum = 0
for i in range(n):
    print(num, end=" ")
    sum += num
    num = (num*10)+1
print(f"\nThe Sum is :{sum}")
