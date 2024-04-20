#Write a Python program to remove characters that have odd index values in a given string.
def odd_values_string(str):
    result = ""

    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]

    return result

print(odd_values_string('abcdef'))  # Output: 'ace'
print(odd_values_string('python'))  # Output: 'pto'