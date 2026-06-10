#Print a multiplication table from 1 to 10 in a formatted grid.

for x in range(1,11):
    for i in range(1,11):
        result = x * i
        print(result, end=' ')
    print()