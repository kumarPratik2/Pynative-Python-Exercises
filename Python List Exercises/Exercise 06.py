# Given a list of integers, iterate through the items and count how many are even and how many are odd.

Numbers = [10, 21, 4, 45, 66, 93, 11]
even_count = 0
for item in Numbers:
    if item % 2 == 0:
        even_count += 1
odd_count = len(Numbers) - even_count
print(f'Even Numbers: {even_count}')
print(f'Odd Numbers: {odd_count}')