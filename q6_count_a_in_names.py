'''Write a program that prompts the user to enter a list of names and store them in a list. The program should display how many times the letter 'a appears within the list.'''

names = input("Enter names separated by commas: ").split(',')
count = sum(name.lower().count('a') for name in names)
print("Total 'a' letters:", count)
