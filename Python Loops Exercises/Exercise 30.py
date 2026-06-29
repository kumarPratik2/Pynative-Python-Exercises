#Write a program to remove all duplicate values from a list using a loop, maintaining the original order of elements.

given = [1, 2, 2, 3, 4, 4, 4, 5]

unique_list = []
for i in given:
  if i not in unique_list:
    unique_list.append(i)
print(unique_list)