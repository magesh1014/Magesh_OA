# 1. Write a program in C to display the first 10 natural numbers.
# Expected Output :
# 1 2 3 4 5 6 7 8 9 10

# for i in range(1,11):
#     print(i, end=" ")

# ____________________________________________________________________________________________________________________

# 2.Write a C program to compute the sum of the first 10 natural numbers.
# Expected Output :
# The first 10 natural number is :
# 1 2 3 4 5 6 7 8 9 10
# The Sum is : 55

# sum=0
# print("The first 10 natural number is : ")
# for i in range(1,11):
#     print(i, end=" ")
#     sum += i
# print()
# print("The Sum is :", sum)
    
# ___________________________________________________________________________________________________________________

# 3. Write a program in C to display n terms of natural numbers and their sum.
# Test Data : 7
# Expected Output :
# The first 7 natural number is :
# 1 2 3 4 5 6 7
# The Sum of Natural Number upto 7 terms : 28 

# terms = int(input("How many terms to be printed: "))
# sum=0
# print(f"The first {terms} natural number is : ")
# for i in range(1,terms+1):
#     print(i, end=" ")
#     sum += i
# print()
# print("The Sum is :", sum)

# ____________________________________________________________________________________________________________________

# 4. Write a program in C to read 10 numbers from the keyboard and find their sum and average.
# Expected Output :
# The sum of 10 no is : 55
# The Average is : 5.500000

# print("Enter 10 numbers :")
# sum = 0
# count=0
# for i in range(1,11):
#     num = int(input(f"Number {i} : "))
#     sum+=num
#     count+=1
#     avg = sum/count
# print(f"The sum of 10 numbers is : {sum} ")
# print(f"The Average is : {avg}")

# _____________________________________________________________________________________________________________________

# 5. Write a program in C to display the cube of the number up to an integer.
# Test Data :
# Input number of terms : 5
# Expected Output :
# Number is : 1 and cube of the 1 is :1
# Number is : 2 and cube of the 2 is :8
# Number is : 3 and cube of the 3 is :27
# Number is : 4 and cube of the 4 is :64
# Number is : 5 and cube of the 5 is :125

# num = int(input("Input number of terms: "))

# for i in range(1, num+1):
#     cube = i ** 3
#     print(f"Number is: {i} and cube of {i} is: {cube}")

# ______________________________________________________________________________________________________________________

# 7. Write a program in C to display the multiplier table vertically from 1 to n.
# Test Data :
# Input upto the table number starting from 1 : 8
# Expected Output :
# Multiplication table from 1 to 8
# 1x1 = 1, 2x1 = 2, 3x1 = 3, 4x1 = 4, 5x1 = 5, 6x1 = 6, 7x1 = 7, 8x1 = 8
# ...
# 1x10 = 10, 2x10 = 20, 3x10 = 30, 4x10 = 40, 5x10 = 50, 6x10 = 60, 7x10 = 70, 8x10 = 80

# table = int(input("Input upto the table number starting from 1 :"))
# print(f"Multiplication table from 1 to {table}:")
# for i in range(1,11):
#     for j in range(1,table+1):
#         print(f"{j}x{i}={i*j}", end="       ")
#     print()
        
# ______________________________________________________________________________________________________________________

# 8. Write a C program to display the n terms of odd natural numbers and their sum.
# Test Data
# Input number of terms : 10
# Expected Output :
# The odd numbers are :1 3 5 7 9 11 13 15 17 19
# The Sum of odd Natural Number upto 10 terms : 100 

# terms = int(input("Input number of terms: "))
# sum = 0
# for i in range(1,terms+11):
#     if i%2 != 0:
#         print("The odd numbers are:")
#         print(i, end=" ")
#         sum += i
#     print()
# print(f"The Sum of odd Natural Number upto {i} terms : {sum}")

# _______________________________OR___________________________________________

# n = int(input("Input number of terms: "))
# odd_nums = []
# sum = 0
# for i in range(1,2*n,2):
#     odd_nums.append(i)
#     sum += i
# print(f"The odd numbers are :{odd_nums}")
# print(f"The Sum of odd Natural Number upto {n} terms : {sum}")

# ______________________________________________________________________________________________________________________

# 9. Write a program in C to display a pattern like a right angle triangle using an asterisk.
# The pattern like : 
# *
# **
# ***
# ****

# row = int(input("enter no. of rows: "))
# char = input("character: ")
# for i in range(1,row+1):
#     print(char*i)

# for i in range(4):
#     print("*" * (i + 1))

# _____________________________________________________________________________________________________________________

# 10. Write a C program to display a pattern like a right angle triangle with a number.
# The pattern like :
# 1
# 12
# 123
# 1234

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
        
# ___________________________________________________________________________________________________________________

# 11. Write a program in C to make such a pattern like a right angle triangle 
# with a number which will repeat a number in a row.
# The pattern like :
#  1
#  22
#  333
#  4444
# n = int(input("Enter the number of rows: "))

# for i in range(1, n + 1):
#     print(str(i) * i)

# ______________________________________________________________________________________________________________________
    
# 12. Write a program in C to make such a pattern like a right angle triangle with the number increased by 1.
# The pattern like :
#    1
#    2 3
#    4 5 6
#    7 8 9 10
# num = 1
# for i in range(1,5):
#     for j in range(i):
#         print(num, end = " ")
#         num+=1
#     print()
    
# __________________________________________________________________________________________________________________

# 15. Write a C program to calculate the factorial of a given number.
# Test Data :
# Input the number : 5
# Expected Output :
# The Factorial of 5 is: 120

# num = int(input("Input the number : "))
# fact = 1
# for i in range(1,num+1):
#     fact*=i
# print(f"The Factorial of 5 is : {fact}")

# ____________________________________________________________________________________________________________________

# 16. Write a C program to display the sum of n terms of even natural numbers.
# Test Data :
# Input number of terms : 5
# Expected Output :
# The even numbers are :2 4 6 8 10
# The Sum of even Natural Number upto 5 terms : 30

# n = int(input("Input number of terms :"))
# even = []
# sum = 0
# for i in range(2,2*n+1,2):
#     even.append(i)
#     sum += i
# print(f"The even numbers are : {even}")
# print(f"The Sum of even Natural Number upto 5 terms : {sum}")

# ________________________________________________________________________________________________________

# 19. Write a program in C to display the n terms of a harmonic series and their sum.
# 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms
# Test Data :
# Input the number of terms : 5
# Expected Output :
# 1/1 + 1/2 + 1/3 + 1/4 + 1/5 +
# Sum of Series upto 5 terms : 2.283334

# n = int(input("Input the number of terms : "))
# sum = 0
# for i in range(1,n+1):
#     print(f"1/{i}", end=" + ")
#     sum += 1/i
# print()
# print(f"Sum of Series upto {n} terms : {sum}")

# ___________________________________________________________________________________________________________________
    




