# Write a script that asks a user for their username using standard input and their password using masked input (where the characters don’t appear on the screen).

import getpass

username = input('Enter your username: ')
password = getpass.getpass('Enter your password: ')

if username == 'admin' and password == '12345':
  print('Login Succesfull')
else:
  print('Username or password error')