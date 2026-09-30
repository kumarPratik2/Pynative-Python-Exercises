#Use the .partition() method to split a string into three parts: the part before a separator, the separator itself, and the part after it.

str1 = 'username@company.com'
sep = '@'

new = str1.partition(sep)
print(new)