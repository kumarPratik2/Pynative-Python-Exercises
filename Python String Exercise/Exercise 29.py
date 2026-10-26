#Write a function to determine if a string has all unique characters. Return True if every character appears only once, otherwise return False.

str1 = input('Enter the string: ').lower().strip()
len1 = len(str1)
set1 = set(str1)
len2 = len(set1)
result = len1 == len2
print(f'"{str1}" unique: {result}')