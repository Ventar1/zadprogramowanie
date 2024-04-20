#Write a Python program that accepts a string and calculates the number of digits and letters.
#Sample Data : Python 3.2
#Expected Output :
#Letters 6
#Digits 2


# Pobierz łańcuch znaków od użytkownika
string = input("Wprowadź łańcuch znaków: ")

# Liczenie liter i cyfr
letters = sum(1 for char in string if char.isalpha())
digits = sum(1 for char in string if char.isdigit())

print("Liczba liter:", letters)
print("Liczba cyfr:", digits)