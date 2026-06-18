#Create a countdown timer that starts from a given number and counts down to zero using a while loop.

import time

t = int(input('Enter time: '))
while t > 0:
  print(t)
  time.sleep(1)
  t -= 1
print('Blast off!')