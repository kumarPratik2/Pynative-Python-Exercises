#Write a program to print a triangle pattern where each row consists of the same letter, and the letter changes (increments) with each new row.

for i in range(1,6):
  ch = chr(64 + i)
  print(ch * i)