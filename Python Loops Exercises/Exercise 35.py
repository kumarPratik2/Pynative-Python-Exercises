#Write a program to check if a number is a “Perfect Number.” A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself). For example, 6 is perfect because 1 + 2 + 3 = 6.

n = 28

factors = []

for i in range(1,n):
  if n%i == 0:
    factors.append(i)
sum = 0
for x in factors:
  sum += x
if n == sum:
  print(f'{n} is a perfect number')
else:
  print(f'{n} is not a perfect number')