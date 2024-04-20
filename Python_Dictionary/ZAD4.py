#5. Write a Python program to iterate over dictionaries using for loops.
# Przykładowy słownik
my_dict = {'apple': 26, 'banana': 18, 'cherry': 35, 'date': 21}

# Iteracja po kluczach
print("Iteracja po kluczach:")
for key in my_dict:
    print(key)

# Iteracja po wartościach
print("\nIteracja po wartościach:")
for value in my_dict.values():
    print(value)

# Iteracja po parach klucz-wartość
print("\nIteracja po parach klucz-wartość:")
for key, value in my_dict.items():
    print(key, "-", value)