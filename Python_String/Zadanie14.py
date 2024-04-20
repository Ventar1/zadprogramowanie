#Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red
items = input("Wprowadź sekwencję słów oddzielonych przecinkami: ")

# Podziel wprowadzone 'items' na listę słów, używając przecinka jako separatora, i zapisz je w liście 'words'.
words = [word.strip() for word in items.split(",")]

print(",".join(sorted(list(set(words)))))