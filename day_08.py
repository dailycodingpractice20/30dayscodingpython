# Dictionaries in python
# Day 8 - 30 Days of Python Daily Coding Challenge

print("Introduction")
print("Day 8 - 30 Days of Python Daily Coding Challenge")
print("Start")

#Creating a dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(person)

#length of dictionary
print(len(person))

#acessing dictionary items
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['country'])
print(person['is_married'])
print(person['skills'])
print(person['address'])
print(person['address']['zipcode'])

#Adding Items to a Dictionary
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

#modifying dictionary
person['first_name'] = 'Eyob'
person['age'] = 252

#Checking Keys in a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

#Removing Key and Value Pairs from a Dictionary
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

#Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

#Clearing a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

#Deleting a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

#Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

#Getting Dictionary Keys as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

#Getting Dictionary Values as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

print("End")
print("Thanks for watching")