#Given a list, iterate it in reverse order and print each element.

list1 = [10, 20, 30, 40, 50]

new = []
n = len(list1)
while n > 0:
  x = list1[n-1]
  new.append(x)
  n -= 1

print(new)
