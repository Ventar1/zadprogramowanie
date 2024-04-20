#Write a Python function that takes two lists and returns True if they have at least one common member.
def have_common_member(list1, list2):
    # Użyj operatora przecięcia `&` zbiorów, aby sprawdzić, czy istnieje wspólny element
    common_elements = set(list1) & set(list2)

    # Sprawdź, czy zbiór wspólnych elementów nie jest pusty
    if common_elements:
        return True
    else:
        return False

# Przykładowe użycie funkcji
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

# Sprawdź, czy listy mają wspólny element i wydrukuj wynik
print("Czy listy mają wspólny element:", have_common_member(list1, list2))
