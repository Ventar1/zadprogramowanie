#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'
def add_ing_ly(str1):
    # Sprawdź, czy długość ciągu 'str1' wynosi co najmniej 3.
    if len(str1) >= 3:
        if str1.endswith('ing'):
            str1 += 'ly'
        else:
            str1 += 'ing'


    return str1


ciag1 = 'abc'
ciag2 = 'string'


print("Dla ciągu '{}' oczekiwany wynik: '{}'".format(ciag1, add_ing_ly(ciag1)))
print("Dla ciągu '{}' oczekiwany wynik: '{}'".format(ciag2, add_ing_ly(ciag2)))