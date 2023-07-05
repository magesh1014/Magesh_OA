# Set Methods

# 1.union()
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}

# set3 = set1.union(set2) 
# print(set3) or print(set1 | set2 )
# output = {1, 2, 3, 4, 5, 6, 7, 8}


# 2.intersection()
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}

# set3 = set1.intersection(set2)
# print(set3)
# output = {4, 5}


# 3.update()
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set1.update(set2)
set1 |= {9,0}
print(set1)
# output = {4, 5}