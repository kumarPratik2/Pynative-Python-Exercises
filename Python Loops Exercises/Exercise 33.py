#Write a program to count the frequency of each word in a given string.

text = "apple banana apple orange banana apple"

fruits = text.split()
counter = {}
for i in fruits:
  if i in counter:
    counter[i] += 1
  else:
    counter[i] = 1
print(counter)