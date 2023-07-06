# find the number and sum of all integers between 100 and 200 which are divisible by 9.
# Expected Output :
# Numbers between 100 and 200, divisible by 9 :
# 108 117 126 135 144 153 162 171 180 189 198
# The sum : 1683 

a = []
sum=0
for i in range(100,201):
    if i%9 == 0:
        a.append(i)
        sum+=i
print(f"Numbers between 100 and 200, divisible by 9 : {a}")
print(f"The sum : {sum}")


