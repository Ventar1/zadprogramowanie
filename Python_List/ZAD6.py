#7. Write a Python program to remove duplicates from a list.
# Zdefiniuj listę 'a' zawierającą kilka duplikujących się i unikalnych elementów
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Utwórz pusty zbiór do przechowywania elementów duplikujących się oraz pustą listę na elementy unikalne
dup_items = set()
uniq_items = []

# Przeiteruj przez każdy element 'x' w liście 'a'
for x in a:
    # Sprawdź, czy bieżący element 'x' nie znajduje się już w zbiorze 'dup_items' (to sprawdzenie duplikatów)
    if x not in dup_items:
        # Jeśli 'x' nie jest duplikatem, dodaj go do listy 'uniq_items'
        uniq_items.append(x)
        # Dodaj 'x' do zbioru 'dup_items', aby oznaczyć go jako już widziany
        dup_items.add(x)

# Wydrukuj zbiór 'dup_items', który teraz zawiera unikalne elementy z pierwotnej listy 'a'
print(dup_items)

