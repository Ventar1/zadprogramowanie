#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
# Definicja funkcji o nazwie swap_and_combine, która przyjmuje dwa argumenty: str1 i str2.
def swap_and_combine(str1, str2):
    # Zamień pierwsze dwa znaki każdego z ciągów.
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:2] + str2[2:]

    # Połącz oba ciągi oddzielone spacją.
    combined_str = swapped_str1 + ' ' + swapped_str2

    # Zwróć połączony ciąg.
    return combined_str

# Przykładowe ciągi wejściowe.
ciag1 = 'abc'
ciag2 = 'xyz'

# Wydrukuj wynik dla przykładowych ciągów.
print("Dla ciągów '{}' i '{}', oczekiwany wynik: '{}'".format(ciag1, ciag2, swap_and_combine(ciag1, ciag2)))
