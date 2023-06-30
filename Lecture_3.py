##operator

##arithmetic operator
'''''
a = int(input("enter a number "))
b = int(input("enter a number "))
print(a + b)
print(a / b) #(always in decimal)
print(a // b)
print(a % b)
print(a * b)
print(a ** b)

a = int(input("enter a number "))
b = float(input("enter a number "))
datatype of int is promoted to float
'''
'''
#agumented operator
a=10
a += 2 #a = a+2 (agumented assignment operator)
print(a)

r = 10
x = r**5
r %= x
print(r)
'''
#logical operator
#and 
#or
#not
'''
a , b = 5 , 4
print(a>4 and b<10)
print(a>4 and b<3)

# T T = T
# F T = F
# T F = F 
# F F = F

print(a>4 or b<10)
print(a<4 or b<3)
# T T = T
# T F = T
# F T = T
# F F = F

print(not(a)) (true=false / false=true)

'''
#print("h" not in "hello")
'''
amt=0 
unit = int(input("enter no. of electcricity unit "))
if unit<100:
    amt=0
if unit>100 and unit<=200:
    amt=(unit-100)*5
if unit>200:
    amt= 500 + (unit-200)*10
print("amount to pay:", amt)


tax= 0
price= int(input("price of your vechicle: "))

if price<=50000:
    tax=5/100*(price)
if price>50000 and price<=10000:
    tax=10/100*(price)
if price>100000:
    tax=15/100*(price)
print("tax should be paid " , tax)
'''

username = "magesh1007"
password = "magesh1234"

user = input("enter your username : ")
passcode = input("enter your password : ")

if (username == user):
    if (password == passcode):
            print("you are logged in sucessfully")
    else:
        print("invalid credential")
        print("frogetten password")
        changePassword = input("Do you want to change your password: yes/no ")
        if (changePassword =="yes"):
            password = input("enter your new password: ")
            re_enter_your_password = input("re_enter_your_password")
            if (password == re_enter_your_password):
                print("you are logged in sucessfully")
            else:
                print("invalid password")
        if (changePassword == "no"):
            print("thank you")
  
        
        