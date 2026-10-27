#Given two strings of equal length, merge them by alternating characters.

str1 = input('Enter a string: ')
str2 = input('Enter a string: ')
n = len(str1)
new_string = ''
for i in range(n):
  new_string += str1[i] + str2[i]
print(new_string)