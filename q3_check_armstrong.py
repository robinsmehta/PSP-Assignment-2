#Write a function to check whether the given number is Armstrong or not.
'''Check if a number is an Armstrong number'''

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == n

num = int(input("Enter a number: "))
print("Armstrong number?", is_armstrong(num))
