#17. Write a Python program to remove duplicates from the dictionary.
# Przykładowy słownik z duplikatami
my_dict = {'apple': 26, 'banana': 18, 'cherry': 35, 'date': 21, 'banana': 18}

# Usuwanie duplikatów
unique_dict = {k: v for k, v in my_dict.items()}

print("Słownik po usunięciu duplikatów:", unique_dict)