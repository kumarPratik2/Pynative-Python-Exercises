#Create a program that takes an integer and prints its multiplication table from 1 to 10.

n = int(input('Enter a number: '))

for i in range(1,11):
  x = n*i
  print(x)