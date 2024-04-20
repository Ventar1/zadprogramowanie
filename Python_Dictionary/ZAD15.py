#16. Write a Python program to get a dictionary from an object's fields.
# Przykładowy obiekt
class Example:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

# Tworzenie słownika na podstawie pól obiektu
obj = Example()
obj_dict = vars(obj)

print("Słownik na podstawie pól obiektu:", obj_dict)