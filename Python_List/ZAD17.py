#Write a Python program to generate all permutations of a list in Python.
from itertools import permutations

def generate_permutations(input_list):
    # Użyj funkcji permutations z modułu itertools, aby wygenerować wszystkie permutacje listy
    perms = permutations(input_list)
    # Przekształć wynikowe permutacje z obiektu generatora na listę permutacji
    all_permutations = list(perms)
    return all_permutations

# Przykładowa lista
my_list = [1, 2, 3]

# Wygeneruj wszystkie permutacje listy i wydrukuj wynik
print("Permutacje listy:", generate_permutations(my_list))
