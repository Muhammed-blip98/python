# Variables vary, They can change. They make our lives easier.

# I like to think of variables as a container used to store specific objects.
# The objects are known as data, and the variables holds data.

# Variable Declaration

first_name = "bwave"   # text string
last_name = "ict"      # text string
age = 10               # number int
score = 45.7           # float decimal
developer = True       # boolean
question = 60 > 10

# Getting user input in python is relatively easy.

# First we declare the variable, then we use a function ask to store the users input into
# the variable, finally we print the input on the screen

first_name = input("What is your name? ")

print("Hello, first_name")

# First we declare the variable, then we use a function ask to store the users input into
# the variable, finally we print the input on the screen

first_name = input("What is your name? ")

print(f"Hello, welcome Mr {first_name} ")

# We can convert variables from one data type to the other. For example, we can get a number
# from a user as a string, but store it as a number.

score = float(input('Enter your score: '))

score /= 2

print(f'Your final score is {score}')