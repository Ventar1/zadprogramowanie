#Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String
# Zdefiniuj funkcję o nazwie string_both_ends, która przyjmuje jeden argument, 'str'.
def string_both_ends(str):
    # Sprawdź, czy długość ciągu wejściowego 'str' jest mniejsza niż 2 znaki.
    if len(str) < 2:
        # Jeśli ciąg jest krótszy niż 2 znaki, zwróć pusty ciąg.
        return ''

    # Jeśli ciąg ma co najmniej 2 znaki, połącz dwa pierwsze znaki
    # i dwa ostatnie znaki ciągu wejściowego i zwróć wynik.
    return str[0:2] + str[-2:]

# Wywołaj funkcję string_both_ends z różnymi ciągami wejściowymi i wydrukuj wyniki.
print(string_both_ends('w3resource'))  # Wynik: 'w3ce'
print(string_both_ends('w3'))          # Wynik: 'w3w3'
print(string_both_ends('w'))           # Wynik: ''