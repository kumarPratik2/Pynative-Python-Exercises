# Accept an integer from the user and display its value in binary format (Base 2).
decimal = int(input('Enter the number you want to convert: '))

binary = ''
num = decimal
while num > 0:
  rem = num % 2
  num = num // 2
  binary = str(rem) + binary 
print(binary)