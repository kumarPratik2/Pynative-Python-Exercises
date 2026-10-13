#Write a program to remove all special symbols and punctuation from a given string.

str1 ='/*Jon is @developer & musician!!'

new_str = ''
for item in str1:
  if item.isalnum() or item.isspace():
    new_str += item
print(new_str)