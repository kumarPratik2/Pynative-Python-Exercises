#Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.

data = "Loops are Fun!"
vowels = ['a', 'e', 'i', 'o', 'u']
data = data.lower()
alphabets = []
count = 0

for i in data:
  x = i.isalpha()
  if x == True:
    alphabets.append(i)

for a in alphabets:
  if a in vowels:
    count += 1

consonant = len(alphabets) - count

print(f'Vowels: {count}')
print(f'Consonats: {consonant}')
