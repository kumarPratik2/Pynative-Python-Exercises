#rite a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

def power(x,y):
    res = x**y
    print(f'{x} raise to the power {y} is {res}')

a = int(input('Enter the base number: '))
b = int(input('Enter the power: '))

power(a,b)