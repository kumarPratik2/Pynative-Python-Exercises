#Write a program to reverse a given integer number (e.g., 76542 should become 24567).

data = 76542

new = ''

n = len(str(data))

for i in range(1,n+1):
  x = (data % (10**i))//(10**(i-1))
  data = data -x
  new  = new + str(x)
print(new)