#Write a script to swap the positions of two elements in a list based on their indices.

number = [23, 65, 19, 90]
a = int(input('Enter the first index you want to swap:'))
b =int(input('Enter the second index you want to swap:'))
number[a], number[b] = number[b], number[a]
print(f'Swapped list: {number}')