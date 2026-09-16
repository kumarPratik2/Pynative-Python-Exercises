#Write a program to split a given string on hyphens and display each substring.

str1 = 'Emma-is-a-data-scientist'

print('Displaying each substring:')
new_str = str1.split('-')
for item in new_str:
  print(item)