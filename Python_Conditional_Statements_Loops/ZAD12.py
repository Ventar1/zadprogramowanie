#12. Write a Python program that accepts a sequence of lines (blank line to terminate)
#as input and prints the lines as output (all characters in lower case).
print("Wprowadź linie (pusty wiersz aby zakończyć):")
lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line.lower())

# Drukowanie linii w małych literach
print("Linie w małych literach:")
for line in lines:
    print(line)
