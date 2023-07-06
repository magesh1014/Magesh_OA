a = input("enter a number: ")
b = 0
for i in a:
    b += int(i)**len(a)
if b == int(a):
    print("armstrong no.")  
else:
    print("not a armstrong no.")