bits = [False,True,False,True,True,False]
new_bits = []

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)
print(bits)
print(new_bits)
print()

super_bits = [ 1 if b == True else 0 for b in bits]

print(super_bits)