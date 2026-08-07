# Ask the user for a numerator and a denominator. Calculate the percentage (numerator/denominator * 100) and display it with exactly two decimal places followed by a percent sign.

numerator = int(input('Enter numerator: '))
denominator = int(input('Enter denominator: '))

if denominator > 0:
  percentage = (numerator*100)/denominator
else:
  print('Denominator cannot be zero')
print('%.2f' %percentage + '%')