# Write a function that takes a list of strings and returns a new list containing only the strings with a length greater than 5 characters.
# Write a function that receives a tuple containing three numbers and returns the largest and smallest numbers as a tuple.
# Write a function with a default parameter for a discount percentage. The function should receive a product price and return the final price after applying the discount.
# Write a function that takes a list of integers and returns a new list containing only the numbers that are greater than 10.
# Write a function that receives a student's name and three test scores and returns a tuple containing the student's name, average score, and True or False indicating whether the student passed.

def long_strings(words):
    return [word for word in words if len(word) > 5]

print(long_strings(["apple", "banana", "cat", "orange", "dog"]))

def largest_smallest(numbers):
    return (max(numbers), min(numbers))

print(largest_smallest((12, 5, 20)))

def final_price(price, discount=10):
    return price - (price * discount / 100)

print(final_price(100))
print(final_price(100, 20))


def greater_than_ten(numbers):
    return [number for number in numbers if number > 10]

print(greater_than_ten([5, 12, 8, 15, 20, 3]))

def student_result(name, score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    passed = average >= 50

    return (name, average, passed)

print(student_result("Muhammed", 70, 80, 60))
