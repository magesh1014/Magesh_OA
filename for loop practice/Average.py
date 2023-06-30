a=input()
b=str(a)
print(b.split(","))
sum = 0
count = 0
for i in b:
    sum += i
    count+=1
    avg=sum/count
    print(avg)
