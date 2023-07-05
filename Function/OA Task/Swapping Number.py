def swap(n1, n2):
    print(f"Before Swapping n1 = {n1} and n2 = {n2}")
    n1,n2 = n2,n1
    print(f"After Swapping n1 = {n1} and n2 = {n2}")
    
num1 = int(input("Input the 1st Number : "))
num2 = int(input("Input the 2nd Number : "))

swap(num1,num2)