#Create a string made of the first, middle, and last character

str1 = 'James'

n = len(str1)
x = n // 2
new_string = str1[0] + str1[x] + str1[-1]
print(new_string)