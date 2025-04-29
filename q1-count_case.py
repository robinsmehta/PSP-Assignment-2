#Write a function that accepts a string and calculates the number of uppercase and lowercase letters.
''' 
This program accepts a string and calculates 
the number of uppercase and lowercase letters.
'''

def count_case(text):
    upper = 0
    lower = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

# Example use
user_input = input("Enter a string: ")
count_case(user_input)
