# Creating a dictionary with fruit names as keys and their colors as values
fruit_colors = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Grapes": "Purple"
}

# Accessing the color of an Apple
apple_color = fruit_colors["Apple"]
print(apple_color)  # Output: Red

# Adding a new fruit
fruit_colors["Orange"] = "Orange"

# Updating the color of Grapes
fruit_colors["Grapes"] = "Green"
print(fruit_colors)

# Removing a fruit using del
del fruit_colors["Banana"]

# Removing a fruit using pop
grapes_color = fruit_colors.pop("Grapes")
print(fruit_colors)
print(grapes_color)  # Output: Green


# Iterating over keys
for fruit in fruit_colors.keys():
    print(fruit)

# Iterating over values
for color in fruit_colors.values():
    print(color)

# Iterating over key-value pairs
for fruit, color in fruit_colors.items():
    print(f"{fruit}: {color}")

# Checking if a key exists
if "Apple" in fruit_colors:
    print("Apple is in the dictionary")
else:
    print("Apple is not in the dictionary")



import json

# Step 2: Read the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Step 3: Inspect the data
print(data)

# Step 4: Accessing Data
students = data["students"]

# Step 5: Process the Data
for student in students:
    name = student["name"]
    age = student["age"]
    grades = student["grades"]
    print(f"{name} ({age}): {grades}")

# Step 6: Modify the Data
new_student = {"name": "Charlie", "age": 21, "grades": [88, 90, 85]}
students.append(new_student)
print(data)

