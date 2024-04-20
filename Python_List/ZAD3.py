#3. Write a Python program to get the largest number from a list.
# Zdefiniuj funkcję o nazwie max_num_in_list, która przyjmuje listę 'list' jako dane wejściowe
def max_num_in_list(list):
    # Zainicjuj zmienną 'max' pierwszym elementem listy wejściowej jako początkowe maksimum
    max = list[0]
    # Przeiteruj przez każdy element 'a' w liście wejściowej 'list'
    for a in list:
        # Sprawdź, czy bieżący element 'a' jest większy od bieżącego maksimum 'max'
        if a > max:
            # Jeśli 'a' jest większe, zaktualizuj maksimum 'max' na 'a'
            max = a
    # Zwróć końcową wartość maksimum w liście
    return max

# Wywołaj funkcję max_num_in_list z listą [1, 2, -8, 0] jako dane wejściowe i wydrukuj wynik
print(max_num_in_list([1, 2, -8, 0]))
