#13. Write a Python program to map two lists into a dictionary.
# Dwie przykładowe listy
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Mapowanie list na słownik
mapped_dict = dict(zip(keys, values))

print("Słownik zmapowany z dwóch list:", mapped_dict)