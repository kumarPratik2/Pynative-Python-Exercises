#Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
y = 0
for x in range(10):
    s = x + y
    print(f'Current number: {x}, Previous number{y}. Sum: {s}')
    y = x
    x += 1