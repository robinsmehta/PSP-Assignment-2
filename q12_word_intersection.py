#Create a function called word_intersection that prompts the user for two English words, and displays which letters the two words have in common.
'''Find common letters between two words'''

def word_intersection():
    w1 = input("Enter first word: ")
    w2 = input("Enter second word: ")
    common = set(w1) & set(w2)
    print("Common letters:", ''.join(sorted(common)))

word_intersection()
