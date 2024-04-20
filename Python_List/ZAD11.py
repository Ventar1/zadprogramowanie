#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
def remove_elements(input_list):
    # Usuń elementy o indeksach 0, 4 i 5, używając wycinków
    input_list = input_list[1:4] + input_list[6:]
    return input_list

# Przykładowa lista
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Usuń określone elementy i wydrukuj listę wynikową
print("Expected Output:", remove_elements(sample_list))
