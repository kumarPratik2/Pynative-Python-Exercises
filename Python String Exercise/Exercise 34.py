# Write a program to find the longest word in a given sentence. If there is a tie, return the first one found.

str1 = 'The quick brown fox jumps over the lazy dog'

list1 = str1.split()
largest = len(list1[0])
winner = list1[0]
for n in range(1,len(list1)):
  if largest < len(list1[n]):
    largest = len(list1[n])
    winner = list1[n]
print(winner)