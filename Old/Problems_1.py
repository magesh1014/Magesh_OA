#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. 
#Ask user for their salary and year of service and print the net bonus amount.
'''
print("enter you salary: ")
salary = int(input())
print("enter your year of service: ")
year_of_service = int(input())

if(year_of_service >5):
    bonus = 5/100*(salary)
    print("net bonus is " , bonus)
else:
    print("need more work experience ")
'''
#Take values of length and breadth of a rectangle from user and check if it is square or no
'''
print("length of the rectangle: ")
l = int(input())
print("breadth of the rectangle: ")
b = int(input())

if (l == b):
    print("therefore it is a square")
else:
    print("it is not a square ")
'''

#Take two int values from user and print greatest among them.
'''
a = int(input("enter a number 1: "))
b = int(input("enter a number 2: "))
if a>b:
    print("greatest is", b)
elif b>a:
    print("greatest is", b)
else:
    print("both are equal")
'''
#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.
'''
print("No. Of Quantity Purchased ")
price = 0
quantity = int(input())

if quantity>100:
    price = (100*quantity)-(10/100*quantity)
    print(price)
else:
    price = 100*quantity
    print(price)
'''
#A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.
'''
print("enter your marks: ")
marks = int(input())

if marks<25:
    print("f")
elif marks>25 and marks<45:
    print("e")
elif marks>45 and marks<50:
    print("d")
elif marks>50 and marks<60:
    print("c")
elif marks>60 and marks<80:
    print("b")
else:
    marks >80
    print("a")
'''
#Take input of age of 3 people by user and determine oldest and youngest among them.
'''
print("enter 1st age")
age1 = int(input())   
print("enter 2nd age")
age2 = int(input())
print("enter 3rd age")
age3 = int(input())

if age1>age2 and age1>age3:
    print("oldest is ", age1)
elif age2>age1 and age2>age3:
        print("oldest is ", age2)
elif age3>age1 and age3>age2:
    print("oldest is ", age3)
else:
    print("all are equal age")
'''
#Write a program to print absolute vlaue of a number entered by user. E.g.-
#INPUT: 1        OUTPUT: 1
#INPUT: -1        OUTPUT: 1
'''
print("enter a number: ")
no = int(input())
if no<0:
    value = no* (-1)
    print(value)
else:
    print(no)
'''
#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
'''
print("number of classes held: ")
noh = int(input())
print("number of clsses attended: ")
noa = float(input())
attendance = (int(noa)/float(noh))*100
if attendance<=75:
    print("you are not alligible to write exam", attendance)
else:
    print("you are elligible to write exam ", attendance)
'''    
#Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
"""
print("do you have medical cause:(yes/no) ")
mc = input()
if mc == "yes" :
    print("you are elligible to write exam ")
else:
    print("number of classes held: ")
    noh = int(input())
    print("number of clsses attended: ")
    noa = float(input())
    attendance = (int(noa)/float(noh))*100
if attendance<=75:
    print("you are not alligible to write exam", attendance)
else:
    print("you are elligible to write exam ", attendance) 
"""
#Write a program to check if a year is leap year or not.
#If a year is divisible by 4 then it is leap year but 
# if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
'''
print("enter a year: ")
year = int(input())
if int(year)%4 == 0:
    print("it is a leap year ")
elif year == (2000,1900,2100) :
    cyear = year%400 
    cyear == 0
    print("it is a leap year ")
else:
    print("it is not a leap year")
'''
#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and 
# then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR".
'''
print("enter your age: ")
age = int(input("age: "))
print("sex: ")
sex = input("M/F: ")
print("martial status: ")
ms = input("Y/N: ")
if sex == "F":
    print("urban areas")
elif sex == "M" and age>=20 and age<=40:
    print("anywhere")
elif sex == "M" and age>=40 and age<=60:
    print("urban")
else:
    print("error")
'''
#A 4 digit number is entered through keyboard. Write a program to 
# print a new number with digits reversed as of orignal one. 
# E.g.-
#INPUT : 1234        OUTPUT : 4321
#INPUT : 5982        OUTPUT : 2895

# Python program to reverse a number
'''
print("enter a 4 digit number: ")
no = str(input())
print(str(no[-1:-5:-1]))
'''