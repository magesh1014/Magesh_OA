# Write a program that prints the multiplication table of a given number up to a specified range.

table = int(input("The Multiplication Table of: "))
for i in range(1,11):
    print(table,"X",i,"=",table*i)