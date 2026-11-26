#Given a list, extract a “slice” containing the middle three elements.

number = [10, 20, 30, 40, 50, 60, 70]

n = len(number)//2
new = number[n-1 : n + 2]
print(new)