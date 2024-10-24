from collections import defaultdict

# Create a defaultdict with default value of 0
my_dict = defaultdict(int)

# Adding keys
my_dict['a']  # This will automatically initialize 'a' with the default value 0
my_dict['b'] += 1  # Incrementing value of 'b'

print(my_dict)  # Output: defaultdict(<class 'int'>, {'a': 0, 'b': 1})


# Create a dictionary with default values using a comprehension
keys = ['a', 'b', 'c']
default_value = 0

my_dict = {key: default_value for key in keys}

print(my_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}


for x in range(97, 102)
       chr(x)             