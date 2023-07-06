# read 10 numbers from the keyboard and find their sum and average.
# Expected Output :
# The sum of 10 no is : 55
# The Average is : 5.500000

print("Enter 10 numbers :")
sum = 0
count=0
for i in range(1,11):
    num = int(input(f"Number {i} : "))
    sum+=num
    count+=1
    avg = sum/count
print(f"The sum of 10 numbers is : {sum} ")
print(f"The Average is : {avg}")