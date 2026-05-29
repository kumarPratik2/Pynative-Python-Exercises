#Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
def fact(n):
    a = n
    for i in range(1,n):
        f = n*i
        n = f
    print(f'Factorial of {a} is {f}.')

x = int(input('Enter a number: '))
fact(x)