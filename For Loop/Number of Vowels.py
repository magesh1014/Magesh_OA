vowel = input("ENTER A STRING: ")
a = 0
for letter in vowel:
    if letter in "aeioAEIOU":
        a +=1
print(a)