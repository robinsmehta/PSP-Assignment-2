'''Write a program that prompts the user for a series of integers and stores in a list only the values between 1-100, and displays the resulting list'''

nums = []
while True:
    val = input("Enter a number (or 'done' to finish): ")
    if val.lower() == 'done':
        break
    num = int(val)
    if 1 <= num <= 100:
        nums.append(num)

print("Numbers between 1-100:", nums)
