#Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.

n = 20
prime = []

for x in range(2, n+1):
    isPrime = True
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            isPrime =   False
            break

    if isPrime == True:
        prime.append(x)
print(prime)