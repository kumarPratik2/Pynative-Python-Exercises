#Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

num = int(input('Enter a number you want to check: '))
reverse = 0
n = len(str(num))
for i in range(n):
    a = ((num//10**i)%10)*10**((n-1)-i)
    reverse = reverse + a


if num == reverse:
    print(f'{num} is a palindrome')
else:
    print(f'{num} is not a palindrome')