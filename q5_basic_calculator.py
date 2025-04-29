'''' Create a program called calculator with functions to perform the following arithmetic calculations, each should take two decimal parameters and return the result of the arithmetic calculation in question.[7]
A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Truncated division
F. Modulus
G. Exponentiation
'''
#'''Calculator with basic arithmetic operations'''

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def trunc_div(a, b): return a // b
def modulus(a, b): return a % b
def exponent(a, b): return a ** b

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))
print("Truncated Division:", trunc_div(x, y))
print("Modulus:", modulus(x, y))
print("Exponentiation:", exponent(x, y))
