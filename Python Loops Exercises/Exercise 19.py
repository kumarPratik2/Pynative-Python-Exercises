#Write a program to check if a number is an Armstrong number. An Armstrong number (for a 3-digit number) is an integer such that the sum of the cubes of its digits is equal to the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).

num = 153

arms = 0

l = len(str(num))

for i in range(1, l+1):
  x = ((num % (10**i)) // (10**(i-1)))**3
  arms += x

if arms == num:
    print(f'{num} is an armstrong number.')

else:
    print(f'{num} is not an armstrong number.')