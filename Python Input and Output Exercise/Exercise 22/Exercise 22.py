#Write a script that checks a file’s metadata. If the file size is 0 bytes, print “File is empty”; otherwise, print the size in bytes.

import os

if os.path.exists('sample.txt'):
  size = os.path.getsize('sample.txt')
  if size == 0:
    print(f'File is empty.')
  else:
    print(f'File is of {size} bytes.')
else:
  print('File not found')