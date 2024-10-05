# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)
# Iterate over a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Iterate over characters in a string
for char in "hello":
    print(char)
# Print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
#functions
# Define a function that prints a personalized greeting
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming.")

# Call the function with a specific name
greet_user("Ayan")
# Define a lambda function that adds two numbers
add = lambda x, y: x + y

# Use the lambda function
print(add(3, 7))

#lists
# Define a list
fruits = ["apple", "banana", "cherry"]

# Print the original list
print("Original list:", fruits)

# Add an element to the list
fruits.append("orange")
print("After adding 'orange':", fruits)

# Insert an element at a specific position
fruits.insert(1, "kiwi")
print("After inserting 'kiwi' at position 1:", fruits)

# Remove an element from the list
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Access elements by index
print("First fruit:", fruits[0])

# Iterate through the list
print("All fruits:")
for fruit in fruits:
    print(fruit)
#tuples
# Define a tuple
colors = ("red", "green", "blue")

# Print the original tuple
print("Original tuple:", colors)

# Access elements by index
print("First color:", colors[0])

# Attempting to modify a tuple will raise an error (tuples are immutable)
# colors[0] = "yellow"  # Uncommenting this line will raise a TypeError

# Iterate through the tuple
print("All colors:")
for color in colors:
    print(color)

# Tuple unpacking
color1, color2, color3 = colors
print("Unpacked colors:", color1, color2, color3)

# Define a set
numbers = {1, 2, 3, 4}

# Print the original set
print("Original set:", numbers)

# Add an element to the set
numbers.add(5)
print("After adding 5:", numbers)

# Add a duplicate element (this will not be added since sets do not allow duplicates)
numbers.add(3)
print("After adding 3 again:", numbers)

# Remove an element from the set
numbers.remove(2)
print("After removing 2:", numbers)

# Check if an element is in the set
print("Is 4 in the set?", 4 in numbers)

# Iterate through the set
print("All numbers in the set:")
for number in numbers:
    print(number)

# Set operations: union, intersection, difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union of set1 and set2:", set1.union(set2))
print("Intersection of set1 and set2:", set1.intersection(set2))
print("Difference of set1 and set2:", set1.difference(set2))





