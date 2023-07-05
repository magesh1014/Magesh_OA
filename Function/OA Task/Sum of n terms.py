def sum():
    n = int(input("INPUT THE NUMBER OF TERMS : "))
    b = 0
    for i in range(1,n+1):
        b += i
    print(f"Sum of {n} terms is {b}")
    
sum()