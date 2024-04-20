def znajdz_najdluzsze_slowo(slowa):
    najdluzsze_slowo = ""
    dlugosc_najdluzszego = 0
    for slowo in slowa:
        if len(slowo) > dlugosc_najdluzszego:
            najdluzsze_slowo = slowo
            dlugosc_najdluzszego = len(slowo)
    return najdluzsze_slowo, dlugosc_najdluzszego

# Przykładowe użycie:
lista_slow = ["Witaj", "świecie", "w", "języku", "Python", "Exercises"]
najdluzsze_slowo, dlugosc = znajdz_najdluzsze_slowo(lista_slow)
print("Najdłuższe słowo:", najdluzsze_slowo)
print("Długość najdłuższego słowa:", dlugosc)