#Write a program to count the total number of vowels (a, e, i, o, u) in a given string.

str1 = 'Hello World'

str1 = str1.lower()
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for item in str1:
  if item in vowels:
    count += 1
print(f'Vowel count: {count}')