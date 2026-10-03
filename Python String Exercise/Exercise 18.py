# Write a program to count all letters, digits, and special symbols from a given string.

str1 = 'P@#yn26at^&i5ve'

alphabet = 0
number = 0
symbol = 0
for item in str1:
  if item.isalpha():
    alphabet += 1
  elif item.isnumeric():
    number += 1
  else:
    symbol += 1
print(f'Total counts of chars, digits, and symbols: Chars = {alphabet} Digits = {number} Symbol = {symbol}')