#Write a program to count the total number of digits in a given integer using a while loop.

number = 75869

n = 0

x = number 
while x > 0:
   n += 1
   x = x // 10
print(n)