#Write a program to check if a given number is a palindrome. A palindrome number is a number that remains the same when its digits are reversed (e.g., 121, 343).

number = 121

reverse = ''

n = len(str(number))

for i in range(1, n+1):
  x = (number % (10**i))//(10**n-1)
  reverse += str(x)

if number == int(reverse):
  print(f'{number} is a palindrome')

else:
  print(f'{number} is not a palindrome')