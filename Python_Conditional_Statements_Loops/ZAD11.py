#11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note :
#i = 0,1.., m-1
#j = 0,1, n-1.
# Funkcja generująca tablicę dwuwymiarową
def generate_2d_array(m, n):
    return [[i * j for j in range(n)] for i in range(m)]

# Testowanie funkcji
rows = 3
columns = 4
result = generate_2d_array(rows, columns)
print("Tablica dwuwymiarowa:", result)