#10. Write a Python program to find the list of words that are longer than n from a given list of words.
def find_words_longer_than_n(word_list, n):
    # Utwórz pustą listę do przechowywania dłuższych słów
    longer_words = []

    # Iteruj przez każde słowo w liście word_list
    for word in word_list:
        # Sprawdź, czy długość bieżącego słowa jest większa niż n
        if len(word) > n:
            # Jeśli tak, dodaj słowo do listy dłuższych słów
            longer_words.append(word)

    # Zwróć listę dłuższych słów
    return longer_words

# Przykładowa lista słów
word_list = ['apple', 'banana', 'orange', 'grape', 'watermelon']

# Określ długość n
n = 5

# Znajdź i wydrukuj listę słów dłuższych niż n
print("Słowa dłuższe niż", n, ":", find_words_longer_than_n(word_list, n))
