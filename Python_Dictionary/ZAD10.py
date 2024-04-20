#11. Write a Python program to multiply all the items in a dictionary.
# Przykładowy słownik
my_dict = {'apple': 2, 'banana': 3, 'cherry': 4, 'date': 5}

# Mnożenie wartości
total_product = 1
for value in my_dict.values():
    total_product *= value

print("Iloczyn wszystkich wartości w słowniku:", total_product)