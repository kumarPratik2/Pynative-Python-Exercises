#Open a file and display only the fourth line of the content.

with open('sample.txt') as f:
  text = f.readlines()
  print(text[3])
  f.close