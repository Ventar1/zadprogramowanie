#Write a Python program to calculate the difference between the two lists.
def calculate_list_difference(list1, list2):
    # Użyj operatora różnicy zbiorów '-' do obliczenia różnicy między listami
    difference = list(set(list1) - set(list2))
    return difference

# Przykładowe listy
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Oblicz różnicę między listami i wydrukuj wynik
print("Różnica między listami:", calculate_list_difference(list1, list2))
