#Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

def pal(x):
    s = str(x)
    z = s[::-1]
    y = int(z)
    if x == y:
        print(f'{x} is a palindrome')
    else:
        print(f'{x} is not a palindrome')

n =int(input('Enter the number you want to check: '))
pal(n)