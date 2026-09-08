#Take a list of favorite fruits and save each fruit onto a new line in a file named fruits.txt.

fruit_list = ["Apple", "Banana", "Cherry", "Date"]

with open("fruits.txt", "w") as f:
  for fruit in fruit_list:
    f.write(fruit + '\n')