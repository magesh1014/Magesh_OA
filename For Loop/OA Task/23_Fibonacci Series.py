# 35. Write a program in C to display the first n terms of the Fibonacci series.
# Fibonacci series 0 1 2 3 5 8 13 .....
# Test Data :
# Input number of terms to display : 10
# Expected Output :
# Here is the Fibonacci series upto to 10 terms :
# 0 1 1 2 3 5 8 13 21 34 
        
terms = int(input("enter no. of terms: "))
n1,n2 = 0,1
sum = 0
for i in range(terms):
    print(sum,end="\t")
    n1 = n2
    n2 = sum
    sum = n1 + n2
    