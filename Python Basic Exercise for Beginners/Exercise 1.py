#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if x*y <= 1000:
    print(f'The product of {x} and {y} is {x*y}.')
else:
    print(f'The sum of {x} and {y} is {x+y}.')