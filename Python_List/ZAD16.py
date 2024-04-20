#Write a Python program to check if each number is prime in a given list of numbers.
 #Return True if all numbers are prime otherwise False.
#Sample Data:
#([0, 3, 4, 7, 9]) -> False
#([3, 5, 7, 13]) -> True
#([1, 5, 3]) -> False
# Zdefiniuj funkcję o nazwie 'is_prime', która sprawdza, czy liczba 'n' jest liczbą pierwszą
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Zdefiniuj funkcję o nazwie 'test', która przyjmuje listę 'nums' jako parametr
def test(nums):
    # Użyj wyrażenia generatora, aby sprawdzić, czy każda liczba w 'nums' jest liczbą pierwszą, i zwróć True, jeśli wszystkie są pierwsze
    return all(is_prime(i) for i in nums)

# Zdefiniuj listę 'nums' zawierającą sekwencję liczb
nums = [0, 3, 4, 7, 9]
# Wydrukuj oryginalną listę liczb
print("Oryginalna lista liczb:")
print(nums)
# Sprawdź, czy każda liczba w 'nums' jest liczbą pierwszą i wydrukuj wynik
print("Sprawdź, czy każda liczba jest liczbą pierwszą w danej liście liczb:")
print(test(nums))

# Przypisz 'nums' do innej listy liczb
nums = [3, 5, 7, 13]
# Wydrukuj oryginalną listę liczb
print("\nOryginalna lista liczb:")
print(nums)
# Sprawdź, czy każda liczba w nowej liście 'nums' jest liczbą pierwszą i wydrukuj wynik
print("Sprawdź, czy każda liczba jest liczbą pierwszą w danej liście liczb:")
print(test(nums))

# Przypisz 'nums' do innej listy liczb
nums = [1, 5, 3]
# Wydrukuj oryginalną listę liczb
print("\nOryginalna lista liczb:")
print(nums)
# Sprawdź, czy każda liczba w nowej liście 'nums' jest liczbą pierwszą i wydrukuj wynik
print("Sprawdź, czy każda liczba jest liczbą pierwszą w danej liście liczb:")
print(test(nums))
