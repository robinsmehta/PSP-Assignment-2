'''Write a program that prompts the user to enter integer values to populate two lists, then prints messages to determine the following:
(a) Whether the lists are of the same length. 
(b) Whether the elements in each list sum to the same value. 
(c) Whether there are any values that occur in both lists
'''

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

print("Same length?", len(list1) == len(list2))
print("Same sum?", sum(list1) == sum(list2))
print("Common values?", bool(set(list1) & set(list2)))
