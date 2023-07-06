# display a pattern like a right angle triangle using an asterisk.
# The pattern like : 
# *
# **
# ***
# ****

row = int(input("enter no. of rows: "))
char = input("character: ")
for i in range(1,row+1):
    print(char*i)

for i in range(4):
    print("*" * (i + 1))