#Write a program to print the pyramid pattern using nested loops:

r = 5
for i in range(1,r+1):
  for j in range(i):
    print('*', end=' ')
  print()
  
for i in range(r-1,1,-1):
  for j in range(i):
    print('* ' * r)
    r-=1
print()