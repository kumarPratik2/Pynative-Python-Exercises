# Write a program to remove all duplicate characters from a string while keeping the remaining characters in their original order.

str1 = input('Enter a string: ')
new_string = ''
for item in str1:
  if item not in new_string:
    new_string += item
print(new_string)