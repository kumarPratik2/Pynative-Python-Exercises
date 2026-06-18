#Write a program to extract each digit from an integer in the reverse order.

def reversal(x):
    y = 0
    n = len(str(x))
    for i in range(0,n):
        a = ((x//10**i)%10)*10**((n-1)-i)
        y = y + a
    print(f'Reverse of {x} is {y}.')

number = int(input('Enter a number: '))
reversal(number)