#Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new = []
n = len(my_list)
for i in range(n):
  if i % 2 != 0:
    x = my_list[i]
    new.append(x)

print(new)