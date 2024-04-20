#Write a Python program to combine two dictionary by adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# Dwa przykładowe słowniki
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Łączenie słowników
merged_dict = {}
for key in set(d1) | set(d2):
    merged_dict[key] = d1.get(key, 0) + d2.get(key, 0)

print("Połączony słownik:", merged_dict)