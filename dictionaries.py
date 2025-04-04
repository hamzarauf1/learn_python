# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# Create dict
person = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 30
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams') 

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

#clear
person.clear()

#get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'kevin', 'age': 25}
]

print(people[0]['name'])