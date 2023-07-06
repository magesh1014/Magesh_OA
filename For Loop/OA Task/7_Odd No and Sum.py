# display the n terms of odd natural numbers and their sum.
# Test Data
# Input number of terms : 10
# Expected Output :
# The odd numbers are :1 3 5 7 9 11 13 15 17 19
# The Sum of odd Natural Number upto 10 terms : 100 

terms = int(input("Input number of terms: "))
sum = 0
for i in range(1,terms+11):
    if i%2 != 0:
        print("The odd numbers are:")
        print(i, end=" ")
        sum += i
    print()
print(f"The Sum of odd Natural Number upto {i} terms : {sum}")

# or

# n = int(input("Input number of terms: "))
# odd_nums = []
# sum = 0
# for i in range(1,2*n,2):
#     odd_nums.append(i)
#     sum += i
# print(f"The odd numbers are :{odd_nums}")
# print(f"The Sum of odd Natural Number upto {n} terms : {sum}")
