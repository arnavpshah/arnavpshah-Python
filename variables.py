
my_list = [] # empty list

my_list = [1, 2, 3, 4, 5] # list of integers

my_list = [1, "Hello", True] # list of mixed values

my_list = ["mouse", [8, 4, 6], ["a"]] # nested lists


my_list = ['p', 'r', 'o', 'b', 'e']




print(my_list[2])


print(my_list[-1]) # negative indexing


n_list = ["Happy", [2, 0, 1, 5]] # nested lists

print(n_list[0][4]) # nested indexing

print(n_list[1][3])

# adding to lists


odd = [2, 4, 6, 8]

odd[0] = 1

odd[1:4] = [3, 5, 7]

print(odd)

odd.extend([9, 11, 13])

print(odd)

# removal of lists and elements

del odd[5]

print(odd)

odd.remove(5)

print(odd)

odd.clear()

print(odd)

# tuple

# unchangeable lists (elements cannot be changed, but can be added/removed)

# no duplicates

even = (2, 4, 6)

even = (2, 4, 6, 8)

# sets

# no duplicates

my_set = {1, 2, 3, 4, 4, 5, 5,5,5,5,5,5, 9}

print(my_set)

my_set = set([1, 2, 3, 2])

print(my_set)

set1 = {1, 3}

print(set1)

set1.update([5, 7, 9])

print(set1)

set1.remove(5)

# dictionaries

# values through key:value pairs

my_dict = {'name': "John", 'age': 26, 'isStudent': False}

print(my_dict['age'])
