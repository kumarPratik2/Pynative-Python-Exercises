#Create a menu that offers three options: “1. Say Hello”, “2. Calculate Square”, and “3. Exit”. The program should perform the action based on the number the user types.

print('''1. Say Hello
2. Calculate a square
3. Exit''')

response = int(input('Enter the choosen option: '))

if response == 1:
  print('Hello! Hope you have a nice day')
elif response == 2:
  number = int(input('Enter the number: '))
  print(f'Square of {number} = {number**2}')
elif response == 3:
  print('Thank You')
else:
  print('Enter Valid response')