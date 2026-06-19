#Write a program that takes a string and reverses it using a for loop. While Python’s [::-1] shortcut is famous, reversing a string manually is a classic way to understand how sequences are constructed.

Input = "Python"

new = ''

for i in Input:
  new = i + new
print(new)