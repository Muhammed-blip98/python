EXCERCISES IN SET
# Exercise 1: Basic Set Operations
# Given two sets:
# colors_1 = {"red", "blue", "green"}
# colors_2 = {"blue", "yellow", "green", "purple"}
# Write Python code to find:
# All unique colors across both sets.
# Colors that are present in both sets.
colors_1 = {"red", "blue", "green"}
colors_2 = {"blue", "yellow", "green", "purple"}
# All unique colors across both sets
unique_colors = colors_1 | colors_2
print("All unique colors:", unique_colors)
# Colors present in both sets
common_colors = colors_1 & colors_2
print("Colors in both sets:", common_colors)

# Exercise 2: Difference & Complement Operations
# Given a set of all registered students all_students = {"Alice", "Bob", "Charlie", "David", "Eve"} and a set of students who submitted their assignment submitted = {"Bob", "David"}:

# Write a Python expression to find the students who have not submitted their assignment.

# Add a new student "Frank" to all_students using the appropriate set method.

# Exercise 8: Filtering Word Lists
# Given a list of words words = ["apple", "banana", "apple", "cherry", "banana", "date"]:

# Convert the list into a set unique_words.

# Write code to check if "cherry" and "grape" exist in unique_words.



# Exercise 3: Filtering Word Lists
# Given a list of words words = ["apple", "banana", "apple", "cherry", "banana", "date"]:

# Convert the list into a set unique_words.

# Write code to check if "cherry" and "grape" exist in unique_words.



SOLUTIONS
1
