# 21. Write a program in C to display the sum of the series [ 9 + 99 + 999 + 9999 ...].
# Test Data :
# Input the number or terms :5
# Expected Output :
# 9 99 999 9999 99999
# The sum of the series = 111105

# n = int(input("Input the number or terms : "))
# num = 9
# sum = 0
# for i in range(n):
#     print(num, end=" ")
#     sum+=num
#     num = (num*10)+9
# print()
# print(f"The sum of the series = {sum}")

# ____________________________________________________________________________________________________________________

# 22. Write a program in C to print Floyd's Triangle.
# 1 
# 01
# 101 
# 0101 
# 10101











# __________________________________________________________________________________________________________________

# 23. Write a program in C to find the sum of the series [x - x^3 + x^5 + ......].
# Test Data :
# Input the value of x :3
# Input number of terms : 5
# Expected Output :
# The sum is : 16.375000 

# value = int(input("Input the value of x : "))
# terms = int(input("Input number of terms : "))
# sum = 0









# _________________________________________________________________________________________________________________

# 25. Write a C program that displays the n terms of square natural numbers and their sum.
# 1 4 9 16 ... n Terms
# Test Data :
# Input the number of terms : 5
# Expected Output :
# The square natural upto 5 terms are :1 4 9 16 25
# The Sum of Square Natural Number upto 5 terms = 55

# n = int(input("Input the number of terms :"))
# sum = 0
# sq = []
# for i in range(1,n+1):
#     power = i**2
#     sq.append(power)
#     sum += power
# print(f"\nThe square natural upto {n} terms are : {sq} ")
# print(f"The Sum of Square Natural Number upto {n} terms = {sum}")

# ___________________________________________________________________________________________________________________

# 26. Write a program in C to find the sum of the series 1 +11 + 111 + 1111 + .. n terms.
# Test Data :
# Input the number of terms : 5
# Expected Output :
# 1 + 11 + 111 + 1111 + 11111
# The Sum is : 12345

# n = int(input("Input the number of terms : "))
# num = 1
# sum = 0
# for i in range(n):
#     print(num, end=" ")
#     sum += num
#     num = (num*10)+1
# print(f"\nThe Sum is :{sum}")

# ___________________________________________________________________________________________________________________

# 27. Write a C program to check whether a given number is a 'Perfect' number or not.
# Test Data :
# Input the number : 56
# Expected Output :
# The positive divisor : 1 2 4 7 8 14 28
# The sum of the divisor is : 64
# So, the number is not perfect.

# divisor = []
# sum = 0
# num = int(input("Input the number : "))

# for i in range(1,num):
#     if num%i == 0:
#         divisor.append(i)
#         sum+=i
# print(f"The positive divisor : {divisor}")
# print(f"The sum of the divisor is : {sum}")
# if num == sum:
#     print("So, the number is perfect.")
# else:
#     print("So, the number is not perfect.")

# ___________________________________________________________________________________________________________________

# 28. Write a C program to find the 'Perfect' numbers within a given number of ranges.
# Test Data :
# Input the starting range or number : 1
# Input the ending range of number : 50
# Expected Output :
# The Perfect numbers within the given range : 6 28
        
# s = int(input("Input the starting range of number : "))
# e = int(input("Input the ending range of number : "))
# perfectnum = []
# for i in range(s,e+1):
#     divisor = []
#     for j in range(s,i):
#         if i%j==0:
#             divisor.append(j)
#     if i == sum(divisor):
#         perfectnum.append(i)
# print(f"The Perfect numbers within the given range : {perfectnum}")
        
#______________________________________________________________________________________________________________________
            
# 30. Write a C program to find the Armstrong number for a given range of number.
# Test Data :
# Input starting number of range: 1
# Input ending number of range : 1000
# Expected Output :
# Armstrong numbers in given range are: 1 153 370 371 407

# s = int(input("Input the starting range of number : "))
# e = int(input("Input the ending range of number : "))

# _____________________________________________________________________________________________________________________

# 32. Write a C program to determine whether a given number is prime or not.
#  Test Data :
# Input a number: 13
# Expected Output :
# 13 is a prime number.

# num = int(input("Input a number: "))

# for i in range(2,num):
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")

# ____________________________________________________________________________________________________________________

# 34. Write a program in C to find the prime numbers within a range of numbers.
# Test Data :
# Input starting number of range: 1
# Input ending number of range : 50
# Expected Output :
# The prime number between 1 and 50 are :
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 

# s = int(input("Input starting number of range: "))   
# e = int(input("Input ending number of range : "))     
# prime_num = []

# for i in range(s,e):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         prime_num.append(i)
# print(f"The prime number between 1 and 50 are : {prime_num} ")

# ___________________________________________________________________________________________________________

# 35. Write a program in C to display the first n terms of the Fibonacci series.
# Fibonacci series 0 1 2 3 5 8 13 .....
# Test Data :
# Input number of terms to display : 10
# Expected Output :
# Here is the Fibonacci series upto to 10 terms :
# 0 1 1 2 3 5 8 13 21 34 
        
# terms = int(input("enter no. of terms: "))
# n1,n2 = 0,1
# sum = 0
# for i in range(terms):
#     print(sum,end="\t")
#     n1 = n2
#     n2 = sum
#     sum = n1 + n2
    
# ______________________________________________________________________________________________________________________

# 37. Write a program in C to display the number in reverse order.
# Test Data :
# Input a number: 12345
# Expected Output :
# The number in reverse order is : 54321
        
# a = input("Input a number: ")
# b = a[::-1]
# print(f"The number in reverse order is : {b}")

# a = input("Input a number: ")
# b = ""
# for i in reversed(a):
#     b+=i
# print(f"The number in reverse order is : {b} ")

# _____________________________________________________________________________________________________________________

# 38. Write a C program to check whether a number is a palindrome or not.
# Test Data :
# Input a number: 121
# Expected Output :
# 121 is a palindrome number.

# a = input("Input a number: ")
# b = ""

# for i in reversed(a):
#     b+=i
# if b == a:
#     print(f"{a} is a palindrome number")
# else:
#     print(f"{a} is not a palindrome number")
    
# ________________________________________________________________________________________________________________
    
# 39. Write a program in C to find the number and sum of all integers between 100 and 200 which are divisible by 9.
# Expected Output :
# Numbers between 100 and 200, divisible by 9 :
# 108 117 126 135 144 153 162 171 180 189 198
# The sum : 1683 

# a = []
# sum=0
# for i in range(100,201):
#     if i%9 == 0:
#         a.append(i)
#         sum+=i
# print(f"Numbers between 100 and 200, divisible by 9 : {a}")
# print(f"The sum : {sum}")

# ____________________________________________________________________________________________________________________

# 43. Write a C program to find the HCF (Highest Common Factor) of two numbers.
# Test Data :
# Input 1st number for HCF: 24
# Input 2nd number for HCF: 28
# Expected Output :
# HCF of 24 and 28 is : 4

# a = int(input("Input 1st number for HCF: "))
