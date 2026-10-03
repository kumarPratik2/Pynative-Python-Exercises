# Write a program to arrange string characters such that all lowercase letters come first, followed by all uppercase letters.

str1 = 'PyNaTive'

upper =''
lower =''
for item in str1:
  if item.islower():
    lower += item
  else:
    upper+= item
new_string = lower + upper
print(new_string)