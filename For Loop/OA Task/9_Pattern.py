# Write a C program to display a pattern like a right angle triangle with a number.
# The pattern like :
# 1
# 12
# 123
# 1234

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print()