# Tuple in python
# Day 6 - 30 Days of Python Daily Coding Challenge

print("Introduction")
print("Day 6 - 30 Days of Python Daily Coding Challenge")
print("Start")

# Empty tuple: Creating an empty tuple
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# Tuple with initial values
print("Tuple with initial values")
tpl = ('item1', 'item2','item3')
print(tpl)
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)

# Tuple length
print("Tuple length")
tpl = ('item1', 'item2', 'item3')
len(tpl)
print(len(tpl))

# Accessing Tuple Items
print("Accessing Tuple Items")
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
print(first_item)
print(second_item)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
print(first_fruit)
print(second_fruit)
print(last_index)
print(last_fruit)

# Syntax Negative indexing
print("Syntax Negative indexing")
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
print(first_item)
print(second_item)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(first_fruit)
print(second_fruit)
print(last_fruit)

# Slicing tuples
print("Slicing tuples")
# Range of Positive Indexes
print("Range of Positive Indexes")
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
print(all_items)
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
print(all_items)
print(middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
print(all_fruits)
all_fruits= fruits[0:]      # all items
print(all_fruits)
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
print(orange_mango)
print(orange_to_the_rest)

# Range of Negative Indexes
print("Range of Negative Indexes")
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
print(all_items)
print(middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)

# Changing Tuples to Lists
print("Changing Tuples to Lists")
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
print(lst)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# Checking an Item in a Tuple
print("Checking an Item in a Tuple")
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# Joining Tuples
print("Joining Tuples")
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print(tpl3)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Deleting Tuples
print("Deleting Tuples")
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

print("End")
print("Thanks for watching")