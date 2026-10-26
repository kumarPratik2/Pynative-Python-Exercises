#Write a program to capitalize the first letter of every word in a sentence without using the built-in .title() method.

str1 = input('Enter a string: ').strip()
list1 = str1.split()
new_list = []
for item in list1:
  item = str(item).capitalize()
  new_list.append(item)
new_string = ' '.join(new_list)
print(new_string)