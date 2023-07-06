terms = int(input("enter no. of terms: "))
n1,n2 = 0,1
sum = 0
for i in range(terms):
    print(sum,end="\t")
    n1 = n2
    n2 = sum
    sum = n1 + n2
    