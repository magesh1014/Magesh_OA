# user1 = int(input("enter no. of rows: "))
# user2 = input("character: ")

# for i in range(user1,0,-1):
#     for j in range(i,0,-1):
#         print(user2, end=" ")
        
#     print()
    
    
user1 = int(input("enter no. of rows: "))
# user2 = input("character: ")

for i in range(user1,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
        
    print()