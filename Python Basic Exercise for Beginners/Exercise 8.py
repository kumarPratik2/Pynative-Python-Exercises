#Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
def reversal(s):
    r = s[::-1]
    print(f'reverse of {s} is {r}')
a = input('Enter a string: ')
reversal(a)