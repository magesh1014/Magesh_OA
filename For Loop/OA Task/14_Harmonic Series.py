
# display the n terms of a harmonic series and their sum.
# 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms
# Test Data :
# Input the number of terms : 5
# Expected Output :
# 1/1 + 1/2 + 1/3 + 1/4 + 1/5 +
# Sum of Series upto 5 terms : 2.283334

n = int(input("Input the number of terms : "))
sum = 0
for i in range(1,n+1):
    print(f"1/{i}", end=" + ")
    sum += 1/i
print()
print(f"Sum of Series upto {n} terms : {sum}")