# Exercise 1: Basic Indexing & Negative Slicing
# Given the tuple:
# colors = ("red", "green", "blue", "yellow", "orange", "purple")
# Write Python expressions to:\
# A: Access the second-to-last element using negative indexing.
# B: Slice and print the middle elements ("green", "blue", "yellow").

colors = ("red", "green", "blue", "yellow", "orange", "purple")

# A: Access the second-to-last element using negative indexing
print(colors[-2])
# B: Slice and print the middle elements ("green", "blue", "yellow")
print(colors[1:4])

# Exercise 2: Tuple Concatenation & Repetition
# Create two tuples:
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# Write code to combine them into a single tuple combined_tup, and then repeat combined_tup twice to form repeated_tup.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
# Concatenate the two tuples
print(t1 + t2)
# Repeat t1 three times
print(t1 * 3)

# Exercise 3: Finding Min, Max, and Sum
# Given a tuple of numerical values:
# data = (42, 17, 89, 23, 56, 99, 4)
# Write code to find and print the minimum, maximum, and total sum of the numbers without using for loops.

data = (42, 17, 89, 23, 56, 99, 4)

# Find and print the minimum
print("Minimum:", min(data))
# Find and print the maximum
print("Maximum:", max(data))
# Find and print the total sum
print("Sum:", sum(data))

# Exercise 4: Nesting and Deep Access
# Given the nested structure:
# nested_record = ("TechCorp", [2024, 2025, 2026], ("HR", "Engineering", "Sales"))

# Write code to:

# Retrieve the year 2025 from the nested list.

# Retrieve the string "Engineering" from the nested inner tuple.

# Exercise 5: Sorting a List of Tuples
# You have a list of student records where each record is a tuple of (name, grade):
# records = [("Alice", 88), ("Bob", 95), ("Charlie", 78), ("Diana", 92)]

# Write Python code to sort the list of tuples in descending order based on the students' grades.

Solutions
