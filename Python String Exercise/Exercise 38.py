#Write a program to check if one string is a rotation of another (e.g., “waterbottle” is a rotation of “erbottlewat”).

str1 = input('Enter a string: ').strip().lower()
str2 = input('Enter a string: ').strip().lower()
rot = False
if len(str1) == len(str2):
  new = str1  + str1
  rot = str2 in new
print(f'Is rotation: {rot}')