#Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
#Sample function and result :
#first_three('ipy') -> ipy
#first_three('python') -> pyt
def first_three(str):
    if len(str) > 3:
        return str[:3]
    else:
        return str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))
