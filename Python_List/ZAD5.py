#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# Zdefiniuj funkcję o nazwie 'last', która przyjmuje pojedynczy argument 'n' i zwraca ostatni element 'n'
def last(n):
    return n[-1]

# Zdefiniuj funkcję o nazwie 'sort_list_last', która przyjmuje listę krotek 'tuples' jako dane wejściowe
def sort_list_last(tuples):
    # Posortuj listę krotek 'tuples', używając funkcji 'last' jako klucza do sortowania
    return sorted(tuples, key=last)

# Wywołaj funkcję 'sort_list_last' z listą krotek jako dane wejściowe i wydrukuj posortowany wynik
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
