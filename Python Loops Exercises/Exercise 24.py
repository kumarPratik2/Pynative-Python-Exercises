# Print a 5*5 square of stars where the middle is empty, leaving only the border.

n = 5
for i in range(n):
  for j in range(n):
    x = '*'
    if i == 0  or i == n-1 or j ==0 or j==n-1:
      print(x, end= '')
    else:
      print(' ', end='')
  print()