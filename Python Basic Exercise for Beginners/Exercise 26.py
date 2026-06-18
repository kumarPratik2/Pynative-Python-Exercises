#Write a program that takes two separate dictionaries and merges them into one single dictionary.

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

for i in dict2:
    dict1.update({i: dict2[i]})
print(dict1)