#Write a Python program to clone or copy a list.
def clone_list(input_list):
    # Użyj operatora przypisania '[:]' do skopiowania listy
    cloned_list = input_list[:]
    return cloned_list

# Przykładowe użycie funkcji
original_list = [1, 2, 3, 4, 5]

# Sklonuj listę i przypisz wynik do nowej zmiennej
cloned_list = clone_list(original_list)

# Wydrukuj oryginalną listę i sklonowaną listę
print("Oryginalna lista:", original_list)
print("Sklonowana lista:", cloned_list)
