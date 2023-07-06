# make a pattern like a right angle triangle with a number which will repeat a number in a row.
# The pattern like :
#  1
#  22
#  333
#  4444

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(str(i) * i)