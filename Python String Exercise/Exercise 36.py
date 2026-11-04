#Count the occurrences of each word in a string and store the result in a dictionary.

str1 = 'apple banana apple cherry banana apple'
str1 = str1.lower().split()
dict1 = {}
for item in str1:
  con = str1.count(item)
  dict1.update({item:con})
print(dict1)