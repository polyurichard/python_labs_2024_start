# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements
first_fruit = fruits[0]
print(first_fruit)

# Modifying elements
fruits[1] = "blueberry"
print(fruits)

# Adding elements
fruits.append("orange")
print(fruits)

# Removing elements
fruits.remove("cherry")
print(fruits)

# Slicing a list
some_fruits = fruits[1:3]
print(some_fruits)

# Looping through a list
for fruit in fruits:
    print(fruit)

# Checking if an item exists
if "apple" in fruits:
    print("Apple is in the list")

# Getting the length of a list
length = len(fruits)
print(length)

# Clearing a list
fruits.clear()
print(fruits)