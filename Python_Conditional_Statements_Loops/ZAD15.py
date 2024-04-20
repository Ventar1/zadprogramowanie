#Write a Python program to check the validity of passwords input by users.
#Validation :

#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.
import re

# Wzorzec dla hasła
password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$')

# Pobierz hasło od użytkownika
password = input("Wprowadź hasło: ")

# Sprawdź poprawność hasła
if re.fullmatch(password_pattern, password):
    print("Poprawne hasło.")
else:
    print("Niepoprawne hasło.")
