#Write a program that accepts 5 float numbers as input from the user and stores them in a list.

List = []
for i in range(1,6):
  a = float(input('Enter a decimal number: '))
  List.append(a)
print(f'User List:{List}')