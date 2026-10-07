#Given a string, run a loop to calculate the add and average of the digits that appear in the string. Ignore all other characters.

str1 ='PYnative29@#8496'

add = 0
digit = []
for item in str1:
  if item.isdigit():
    add = add + int(item)
    digit.append(item)
average = add/len(digit)
print(f'sum is: {add} Average is: {average:,.2f}')