#Write a Python program to get the last part of a string before a specified character.
#https://www.w3resource.com/python-exercises
#https://www.w3resource.com/python

str1 = 'https://www.w3resource.com/python-exercises/string'

print(str1.rsplit('/', 1)[0])  # Output: 'https://www.w3resource.com/python-exercises'

print(str1.rsplit('-', 1)[0])  # Output: 'https://www.w3resource.com/python'
