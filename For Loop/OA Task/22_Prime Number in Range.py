# 34. Write a program in C to find the prime numbers within a range of numbers.
# Test Data :
# Input starting number of range: 1
# Input ending number of range : 50
# Expected Output :
# The prime number between 1 and 50 are :
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 

s = int(input("Input starting number of range: "))   
e = int(input("Input ending number of range : "))     
prime_num = []

for i in range(s,e):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime_num.append(i)
print(f"The prime number between 1 and 50 are : {prime_num} ")