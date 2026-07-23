#Given a 2D list (matrix), find the row and column index of a target value.

matrix = [[10, 20], [30, 40], [50, 60]]
target = 30

for item in matrix:
  if target in item:
    row = matrix.index(item)
    column = item.index(target)
    print(f'row = {row}, column = {column}')