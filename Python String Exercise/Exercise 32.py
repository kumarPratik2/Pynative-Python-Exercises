#Reverse the order of words in a given sentence, but keep the characters within the words in their original order.

str1 = input('Enter a string: ')
list1 = str1.split()
new_string = ' '.join(list1[::-1])
print(new_string)