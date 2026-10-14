#Write a program to extract only the numeric digits from a mixed string and combine them into a single string.

str1 = 'I am 25 years and 10 months old'

new_str = ''
for item in str1:
  if item.isnumeric():
    new_str += item
print(new_str)