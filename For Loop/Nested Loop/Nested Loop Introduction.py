'''
for i in range(1,3):
    for j in range(1,3):
        print(i, j)
'''
        
# i=1
#     j=1|2
# i=2
#     j=1|2

# output:
#     11
#     12
#     21
#     22
    
for i in range(0,3):
    for j in range(0,3):
        for k in range(1,4):
            print(i, j, k)
            
# i=0
#     j=0
#         k=1|2|3
# i=0
#     j=1
#         k=1|2|3
# i=0
#     j=2
#         k=1|2|3
# i=1
#     j=0
#         k=1|2|3
# i=1
#     j=1
#         k=1|2|3
# i=1
#     j=2
#         k=1|2|3
# i=2
#     j=0
#         k=1|2|3
# i=2
#     j=1
#         k=1|2|3
# i=2
#     j=2
#         k=1|2|3