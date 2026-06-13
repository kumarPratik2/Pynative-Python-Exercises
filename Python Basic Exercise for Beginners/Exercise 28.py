#Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.

numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
odd_nubers = []
even_nubers = []

for i in numbers:
    if i % 2 == 0:
        odd_nubers.append(i)
    else:
        even_nubers.append(i)

print(f'Odd numbers: {odd_nubers}')
print(f' Even numbers: {even_nubers}')