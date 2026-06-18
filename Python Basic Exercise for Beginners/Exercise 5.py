#Write a program to swap the values of two variables, a and b, without using a third temporary variable.
def swap(a,b):
    a,b = b,a #this statement swaps the values of variables
    print(f'The numbers after swapping are {a}, {b}')

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
swap(x,y)