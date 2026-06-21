#Write a program to find the largest and smallest digit within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).

num = 75869

num = str(num)

largest = num[0]
smallest = num[0]

for x in num:
  if x >= largest:
    largest = x

for y in num:
  if y <= smallest:
    smallest = y

print(f'Largest digit: {largest}')
print(f'Smallest digit: {smallest}')