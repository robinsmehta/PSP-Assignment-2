#Write a function to check whether the given number is prime or not.
'''Check if a number is prime'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print("Prime number?" , is_prime(num))
