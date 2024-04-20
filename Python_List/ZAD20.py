#Write a Python script to sort (ascending and descending) a dictionary by value.
# Przykładowy słownik
my_dict = {'apple': 26, 'banana': 18, 'cherry': 35, 'date': 21}

# Sortowanie rosnąco po wartościach
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sortowanie malejąco po wartościach
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Posortowany słownik rosnąco:", sorted_dict_asc)
print("Posortowany słownik malejąco:", sorted_dict_desc)
