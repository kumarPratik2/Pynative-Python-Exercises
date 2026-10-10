# Count the frequency of every character in a string and store the results in a dictionary.

str1 = 'apple'

counter = {}
for item in str1:
  n = str1.count(item)
  counter.update({item:n})
print(counter)