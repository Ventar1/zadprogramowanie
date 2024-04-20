#Zgadywanie liczby między 1 a 9
import random

# Wylosuj liczbę
number_to_guess = random.randint(1, 9)

while True:
    # Zapytaj użytkownika o zgadnięcie
    guess = int(input("Zgadnij liczbę między 1 a 9: "))

    # Sprawdź poprawność zgadnięcia
    if guess == number_to_guess:
        print("Dobrze zgadłeś!")
        break
    else:
        print("Nieprawidłowa odpowiedź. Spróbuj ponownie.")
