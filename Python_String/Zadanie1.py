#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')

    # Zrekonstruuj ciąg 'str1', umieszczając oryginalny znak 'char' jako pierwszy znak
    # po którym następuje zmodyfikowany ciąg zaczynający się od drugiego znaku.
    str1 = char + str1[1:]
    return str1

# Wywołaj funkcję change_char z argumentem 'restart' i wydrukuj wynik.
print(change_char('restart'))  # Wynik: 'resta$t'