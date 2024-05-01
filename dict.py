# Buat dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing values in the dictionary
print(person["name"])  # Output: John
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York

# Adding a new key-value pair
person["country"] = "USA"
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Updating a value
person["age"] = 35
print(person)  # Output: {'name': 'John', 'age': 35, 'city': 'New York', 'country': 'USA'}

# Removing a key-value pair
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 35, 'country': 'USA'}


