#Write a Python function to reverse a string if its length is a multiple of 4.
def reverse_string_if_multiple_of_4(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string

# Przykładowe użycie funkcji
print(reverse_string_if_multiple_of_4("abcd"))   # Wyjście: "dcba"
print(reverse_string_if_multiple_of_4("python"))  # Wyjście: "python"
print(reverse_string_if_multiple_of_4("hello"))   # Wyjście: "hello"
print(reverse_string_if_multiple_of_4("abcdefgh"))   # Wyjście: "hgfedcba"
