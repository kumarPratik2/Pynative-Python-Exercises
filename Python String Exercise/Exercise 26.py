#Write a program to replace every special symbol (punctuation) in a string with a specific character, like #.

str1 ='/*Jon is @developer & musician!!'
new_str = ''

for item in str1:
  if item.isalnum() or item.isspace():
    new_str += item
  else:
    new_str += '#'
print(new_str)