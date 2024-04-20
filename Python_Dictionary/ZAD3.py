#4. Write a Python script to check whether a given key already exists in a dictionary.
# Przykładowy słownik
my_dict = {'apple': 26, 'banana': 18, 'cherry': 35, 'date': 21}

# Klucz do sprawdzenia
key_to_check = 'banana'

# Sprawdzenie czy klucz już istnieje
if key_to_check in my_dict:
    print(f"Klucz '{key_to_check}' już istnieje w słowniku.")
else:
    print(f"Klucz '{key_to_check}' nie istnieje w słowniku.")
