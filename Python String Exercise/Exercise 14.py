#Write a program to remove the character at index i from a string.

str1 = 'Python'
i = 2

start = str1[:i]
finish = str1[i+1:]
print(f'After removing index {i}: {start + finish}')