# 12. Write a program in C to make such a pattern like a right angle triangle with the number increased by 1.
# The pattern like :
#    1
#    2 3
#    4 5 6
#    7 8 9 10

num = 1
for i in range(1,5):
    for j in range(i):
        print(num, end = " ")
        num+=1
    print()