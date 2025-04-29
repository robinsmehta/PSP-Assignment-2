'''Create three dictionaries:
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
(a) Write code to concatenate these dictionaries to create a new one. Create a variable called nums to store the resulting dictionary. 

(b) Write code to add a new key/value pair to the dictionary nums: (7, 70)
(c) Write code to update the value of the item with key 3 in nums to 80
(d) Write code to remove the third item from dictionary nums.
(e) Write code to sum all the items in the dictionary nums
(f) Write code to multiply all the items in the dictionary nums
(g) Write code to retrieve the maximum and minimum values in nums.
'''

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

# a. Concatenate
nums = {**dic1, **dic2, **dic3}

# b. Add new pair
nums[7] = 70

# c. Update value for key 3
nums[3] = 80

# d. Remove third item
nums.pop(list(nums.keys())[2])

# e. Sum values
print("Sum:", sum(nums.values()))

# f. Multiply values
result = 1
for v in nums.values():
    result *= v
print("Product:", result)

# g. Max and min
print("Max:", max(nums.values()))
print("Min:", min(nums.values()))
