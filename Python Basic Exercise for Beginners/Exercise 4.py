#Write a function to remove characters from a string starting from index 0 up to n and return a new string.
def remove_char(s, i):
    z = s[i:]
    print(z)

x = input('Enter a string: ')
y = int(input('Enter the index number: '))
remove_char(x,y)