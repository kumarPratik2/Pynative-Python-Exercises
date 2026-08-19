#Read an existing file test.txt and store every line as an individual element in a Python list.

count = 0
with open('test.txt','r') as f:
  for line in f:
    count += 1 
  print(count)