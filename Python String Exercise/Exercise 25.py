#Write a program to find and print words from a string that contain both letters and numbers.

str1 ='Emma25 is Data scientist50 and AI Expert 2!'

new = []
str1 = str1.split()
for item in str1:
  if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
    new.append(item)
print(new)