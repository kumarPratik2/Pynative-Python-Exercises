# Accept an integer from the user and display it as an octal number (Base 8).

decimal = int(input('Enter the number you want to convert: '))

octal = ''
num = decimal
while num > 0:
  rem = num % 8
  num = num // 8
  octal = str(rem) + octal 
print(octal)