# find the sum of the series 1!/1+2!/2+3!/3+4!/4+5!/5 using the function.
# Expected Output :

#  The sum of the series is : 34 
 
def series():
    fact = 1
    sum = 0
    for i in range(1,6):
        fact*=i
        div = fact/i
        sum += div
    print(f"The sum of the series is : {sum}")
    
series()
        
        