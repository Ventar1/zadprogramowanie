#12. Write a Python program to remove a key from a dictionary.
# Przykładowy słownik
my_dict = {'apple': 26, 'banana': 18, 'cherry': 35, 'date': 21}

# Klucz do usunięcia
key_to_remove = 'banana'

# Usunięcie klucza
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Usunięto klucz '{key_to_remove}' ze słownika.")
else:
    print(f"Klucz '{key_to_remove}' nie istnieje w słowniku.")

print("Nowy słownik po usunięciu klucza:", my_dict)
