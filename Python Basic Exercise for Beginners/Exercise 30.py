#Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.

text = "apple banana apple cherry banana apple"

fruits = {}
x = text.split(' ')
for i in x:
    count = x.count(i)
    fruits.update({i : count})
print(fruits)