#Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.

z = []
input_string = "Python3"
for x in input_string:
  y = x.isnumeric()
  if y == True:
    print(f'The string {input_string} contains digits: {y}')