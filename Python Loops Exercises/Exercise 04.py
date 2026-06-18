#Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.

N = int(input('Enter a number: '))
sum = 0
for i in range(N + 1):
  sum = sum + i
print(f'Sum is :{sum}')