def count(word):
    count = {}
    for char in word:
        if char in count:
            count[char]+=1
        else:
            count[char] = 1
    print(f"CHARACTER COUNTING : {count}")
strings = input("ENTER A STRING: ")
count(strings)
