#Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def checker(li):
    if li[0] == li[-1]:
        print(f'given list : {li}| result is true')
    
    else:
        print(f'given list : {li}|result is false')

checker(numbers_x)
checker(numbers_y)