#5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2
# Zdefiniuj funkcję o nazwie match_words, która przyjmuje listę słów 'words' jako dane wejściowe
def match_words(words):
    # Zainicjuj licznik 'ctr' do śledzenia dopasowanych słów
    ctr = 0

    # Przeiteruj przez każde słowo w liście wejściowej 'words'
    for word in words:
        # Sprawdź, czy słowo ma długość większą niż 1 i czy jego pierwszy i ostatni znak są takie same
        if len(word) > 1 and word[0] == word[-1]:
            # Jeśli warunek jest spełniony, zwiększ licznik 'ctr'
            ctr += 1

    # Zwróć końcową liczbę dopasowanych słów
    return ctr

# Wywołaj funkcję match_words z listą ['abc', 'xyz', 'aba', '1221'] jako dane wejściowe i wydrukuj wynik
print(match_words(['abc', 'xyz', 'aba', '1221']))
