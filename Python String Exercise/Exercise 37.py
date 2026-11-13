#Find the first character in a string that does not repeat anywhere else.

str1 = input('Enter a string: ')
frequency = {}
for item in str1:
    n = str1.count(item)
    frequency[item] = n

    if frequency[item] == 1:
        first = item
        break
    else:
        first = None
print(first)