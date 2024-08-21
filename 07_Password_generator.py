import random
import string

# Define a function to generate a password
def generate_password(length, special_char, numbers):
    print("Let me suggest a password for you")

    # Character set for password  
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation.replace(" ", "")

    # Actual calculation for password 
    character = letters
    password = ""
    if special_char and numbers:
        character += special
        character += digits
    elif special_char == 'False' and numbers == 'True':
        character += digits
    elif special_char == 'True' and numbers == 'False':
        character += special
    else:
        print("Something incorrect happened")
        quit()

    while len(password) < length:
        password += random.choice(character)

    print(password)

# Setting up the default value for the parameters
sc = 'True'
num = 'True'

print("Let's generate a password for you")
pass_length = input("Enter the password length: ")

# For special_char
special_char = input("Do you want special characters in your password? Y/N ").lower()
if special_char == "y":
    sc = 'True'
elif special_char == "n":
    sc = 'False'
else:
    print("Incorrect value input")
    quit()

# Ask user for numbers
numbers = input("Do you want numbers in your password? Y/N ").lower()
if numbers == "y":
    num = 'True'
elif numbers == "n":
    num = 'False'
else:
    print("Incorrect value input")
    quit()

generate_password(int(pass_length), sc, num)
