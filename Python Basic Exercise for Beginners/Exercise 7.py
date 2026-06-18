#Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
f = input('Enter the fruit name you want in list: ')
fruits.append(f)
fruits.pop(1) #pop removes items from list of given index
print(fruits)