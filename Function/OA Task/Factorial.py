def fact():
    f = int(input("Input The Number : "))
    a = 1
    for i in range(1,f+1):
        a*=i
    print(f"Factorial of {f} is {a}")
    
fact()