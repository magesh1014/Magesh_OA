# check whether a given number is a 'Perfect' number or not.
# Test Data :
# Input the number : 56
# Expected Output :
# The positive divisor : 1 2 4 7 8 14 28
# The sum of the divisor is : 64
# So, the number is not perfect.

divisor = []
sum = 0
num = int(input("Input the number : "))

for i in range(1,num):
    if num%i == 0:
        divisor.append(i)
        sum+=i
print(f"The positive divisor : {divisor}")
print(f"The sum of the divisor is : {sum}")
if num == sum:
    print("So, the number is perfect.")
else:
    print("So, the number is not perfect.")
