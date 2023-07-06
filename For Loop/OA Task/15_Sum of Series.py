# display the sum of the series [ 9 + 99 + 999 + 9999 ...].
# Test Data :
# Input the number or terms :5
# Expected Output :
# 9 99 999 9999 99999
# The sum of the series = 111105

n = int(input("Input the number or terms : "))
num = 9
sum = 0
for i in range(n):
    print(num, end=" ")
    sum+=num
    num = (num*10)+9
print()
print(f"The sum of the series = {sum}")



