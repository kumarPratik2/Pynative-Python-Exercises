#Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in s1 are present in s2. The character’s position doesn’t matter.

s1 = input('Enter a string: ')
s2 = input('Enter a string: ')

balance = True
for item in s1:
  if item not in s2:
    balance = False
    break
if balance:
  print(f'{s1} is  present in {s2}')
else:
  print(f'{s1} is not present in {s2}')