fruits = ["apple","banana","strawberry"]

# For Loop
for fruit in fruits:
    print(fruit)

# List Comperhension
[ print(fruit) for fruit in fruits ]

# Example
new_fruit = []

for fruit in fruits:
    fruit = fruit.upper()
    new_fruit.append(fruit)
print(new_fruit)

# List Comperhension
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
