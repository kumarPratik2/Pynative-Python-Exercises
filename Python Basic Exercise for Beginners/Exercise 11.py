#Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
data = [1, 2, 2, 3, 4, 4, 4, 5]
unique_list = []
di = {}
count = 0
for i in data:
    if i in data:
        count += 1
    di.update({i:count})
for x in di:
    unique_list.append(x)
print(unique_list)