#8. Write a Python program to check if a list is empty or not.
def is_list_empty(input_list):
    # Sprawdź, czy lista jest pusta
    if not input_list:
        return True
    else:
        return False

# Przykładowe użycie funkcji
empty_list = []
non_empty_list = [1, 2, 3]

# Sprawdź, czy lista jest pusta lub nie i wydrukuj wynik
print("Czy lista pusta:", is_list_empty(empty_list))  # Wynik: True
print("Czy lista pusta:", is_list_empty(non_empty_list))  # Wynik: False
