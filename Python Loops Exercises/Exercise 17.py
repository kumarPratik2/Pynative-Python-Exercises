#Write a program to use a loop to find the factorial of a given number (e.g., 5!). The factorial of N is the product of all integers from 1 to N.

num = 5

fact = num

for i in range(1,num):
  fact *= i

print(fact)