#Accept an integer and display its value in hexadecimal format (Base 16).

def hexadecimal(dec):
  hexadecimal = ''
  Hex = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
  num = dec
  while num > 0:
    rem = Hex[num % 16]
    num = num // 16
    hexadecimal = str(rem) + hexadecimal 
  return hexadecimal

decimal = int(input('Enter the number you want to convert: '))
result = hexadecimal(decimal)
print(result)