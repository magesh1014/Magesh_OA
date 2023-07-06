# check whether a number is a palindrome or not.
# Test Data :
# Input a number: 121
# Expected Output :
# 121 is a palindrome number.

a = input("Input a number: ")
b = ""

for i in reversed(a):
    b+=i
if b == a:
    print(f"{a} is a palindrome number")
else:
    print(f"{a} is not a palindrome number")