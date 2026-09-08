#Write a program that opens an existing text file and calculates exactly how many lines of text it contains.

with open('sample.txt') as f:
  count = 0
  for x in f:
    count += 1
  print(count)