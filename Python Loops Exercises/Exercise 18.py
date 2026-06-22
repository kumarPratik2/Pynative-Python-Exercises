#The Collatz conjecture states that if you start with any positive integer n, and if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. Repeat the process. The sequence will always eventually reach 1. Write a program to print this sequence for a given number.

n = 6
int(n)
print(n, end=' ')

while n > 1:
  if n % 2 == 0:
    n //= 2

  else:
    n = (n * 3) + 1
  
  print(int(n), end=' ')