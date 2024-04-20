def change_string(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]

print(change_string('abcd'))   # Output: 'dbca'
print(change_string('12345'))  # Output: '52341'
