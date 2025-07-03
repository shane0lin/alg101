from sortedcontainers import SortedDict

# Initialize SortedDict
sd = SortedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})

# 'apple' is found at index 0
print(sd.bisect_left('apple'))  # Output: 0
# 'apple' is found before index 1
print(sd.bisect_right('apple'))  # Output: 1

# Remove 'apple' and print the removed item
item = sd.pop('apple')
print('Popped item:', item)  # Output: Popped: 4

# Attempt to fetch a nonexisting key
value = sd.get('apple', 'Not found')
print('Value:', value)  # Output: Value: Not found

# Peek at the last item
last_item = sd.peekitem()
print('Last item:', last_item)  # Output: Last item: ('pear', 1)