#Write a program that asks the user for a filename and deletes it from the folder. Caution: This operation is permanent.

import os
filename = input('Enter filename which you want to delete: ')
if os.path.exists(filename):
  response = input(f'Do you want to delete {filename} permanently? y/n ').lower().strip()
  if response == 'y':
    os.remove(filename)
    print(f'{filename} deleted successfully')
  elif response == 'n':
    print(f'{filename} not deleted')
  else:
    print('Enter valid response')
else:
  print(f'{filename} not found')