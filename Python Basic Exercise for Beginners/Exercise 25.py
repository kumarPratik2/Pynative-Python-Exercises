#Write a program that takes a year as input and determines if it is a leap year.

year = int(input('Enter the year you want to check: '))
if year %4 == 0:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')