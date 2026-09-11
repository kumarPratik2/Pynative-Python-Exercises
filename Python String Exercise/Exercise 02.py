#Create a string made of the middle three characters

str1 = 'JhonDipPeta'

n = len(str1)
x = n // 2
new_string = str1[x-1] + str1[x] + str1[x+1]
print(new_string)