#4. Write a Python program to get the smallest number from a list.
# Zdefiniuj funkcję o nazwie smallest_num_in_list, która przyjmuje listę 'list' jako dane wejściowe
def smallest_num_in_list(list):
    # Zainicjuj zmienną 'min' pierwszym elementem listy wejściowej jako początkowe minimum
    min = list[0]
    # Przeiteruj przez każdy element 'a' w liście wejściowej 'list'
    for a in list:
        # Sprawdź, czy bieżący element 'a' jest mniejszy niż bieżące minimum 'min'
        if a < min:
            # Jeśli 'a' jest mniejsze, zaktualizuj minimum 'min' na 'a'
            min = a
    # Zwróć końcową wartość minimum w liście
    return min

# Wywołaj funkcję smallest_num_in_list z listą [1, 2, -8, 0] jako dane wejściowe i wydrukuj wynik
print(smallest_num_in_list([1, 2, -8, 0]))
