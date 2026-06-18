#Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method.

text = "hello world from python"
n = text.split()
for i in n:
  x = i.capitalize()
  print(x, end=' ')