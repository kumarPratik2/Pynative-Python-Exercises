#Print a downward number pattern where each row starts with a decreasing value.

for i in range(5,0,-1):
  for j in range(i,0, -1):
    print(j, end=' ')
  print()