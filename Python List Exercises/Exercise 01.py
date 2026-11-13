#Write a script to perform the following three operations on given list
# Access the third element of a list
# List Length: Print the total number of items
# Check if the list is empty

numbers = [10, 20, 30, 40, 50]

third = numbers[2]
print(f'Third Element of list: {third}')

length = len(numbers)
print(f'Length of list: {length}')

empty = length == 0
print(f'Is the list empty?: {empty}') 