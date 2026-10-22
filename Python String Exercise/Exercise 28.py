#Write a program to check if two strings are anagrams (formed by rearranging the letters of another, such as “listen” and “silent”).

s1 = input('Enter first string: ').strip().lower()
s2 = input('Enter second string: ').strip().lower()
anag = sorted(s1) == sorted(s2)
print(f'Is anagram: {anag}')