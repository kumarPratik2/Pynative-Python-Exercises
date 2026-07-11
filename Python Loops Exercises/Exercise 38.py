# Write a program to display all prime numbers within a range (e.g., 25 to 50). A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

x = 25
y = 39
prime = []
for n in range(x,y+1):
  isPrime = True
  for i in range(2, int(n**(1/2))+1):
    if n % i == 0:
      isPrime = False
      break
  if isPrime == True:
    prime.append(n)
print(prime)