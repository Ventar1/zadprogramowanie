#14. Write a Python program to sort a given dictionary by key.
# Przykładowy słownik
my_dict = {'banana': 18, 'date': 21, 'apple': 26, 'cherry': 35}

# Sortowanie po kluczach
sorted_dict = dict(sorted(my_dict.items()))

print("Słownik posortowany po kluczach:", sorted_dict)