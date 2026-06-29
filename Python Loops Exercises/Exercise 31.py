#Given a list of integers, move all even numbers to the beginning of the list and all odd numbers to the end.

numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []
for item in numbers:
  if item % 2 == 0:
    even.append(item)
  else:
    odd.append(item)

Segregated_List = even + odd
print(Segregated_List)