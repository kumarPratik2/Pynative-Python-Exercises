# Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new =[]
for x in list1:
    if x % 2 == 1:
        new.append(x)

for y in list2:
    if y % 2 == 0:
        new.append(y)
print(f'Expected output: {new}')