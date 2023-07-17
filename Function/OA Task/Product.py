def product(a):
    p = 1
    for i in a:
        if i != 0:
            p*=i
    return p

print(product([1,2,3,4,0]))
print(product([0,9,8,7,6]))
