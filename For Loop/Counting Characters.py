word = input("ENTER A STRING: ")
count = {}
for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(f"{char}:{count}")