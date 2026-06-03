#Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

v = ('a', 'e', 'i', 'o', 'u')
count = 0
text = 'python is fun'
for x in text:
    if x in v:
        count +=1
print(count)
