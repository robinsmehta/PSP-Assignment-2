'''Write a function to accept a list of names and return the sorted order of names back'''

def sort_names(names):
    return sorted(names)

names = input("Enter names separated by commas: ").split(',')
print("Sorted names:", sort_names(names))
