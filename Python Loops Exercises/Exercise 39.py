#Given a nested list (a list containing other lists), write a program to “flatten” it into a single list containing all the individual elements.

nested_list = [[10, 20], [30, 40], [50, 60]]

flat_list = []
for item in nested_list:
  for number in item:
    flat_list.append(number)
print(flat_list)