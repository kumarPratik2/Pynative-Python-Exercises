#Create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).

square = {}
for x in range(1,11):
    y = x**2
    square.update({x : y})
print(square)