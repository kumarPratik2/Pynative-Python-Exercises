#Write a program to check if a string is a palindrome (reads the same forward and backward).

str1 = 'Radar'

str1 = str1.lower().strip()
new_str = str1[::-1]
pal = str1 == new_str
print(f'Is palindrome: {pal}')