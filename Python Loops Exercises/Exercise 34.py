#Write a program to display the Fibonacci sequence up to 10 terms. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

n = 10

fibonacci = [0,1]

for i in range(n-2):
  a = fibonacci[i] + fibonacci[i+1]
  fibonacci.append(a)
print(fibonacci)