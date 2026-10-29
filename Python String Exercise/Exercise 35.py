#Write a program to generate an acronym from a given phrase (e.g., “Random Access Memory” becomes “RAM”).

str1 = input('Enter a string: ')
acro = ''
list1 = str1.split()
for item in list1:
  acro += item[0].upper()
print(acro)