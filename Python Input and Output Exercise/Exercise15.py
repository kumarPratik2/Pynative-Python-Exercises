#You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78]. Print these as a table with aligned columns.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f'{'Name':<10} {'Score'}')
print('-' * 15)

for name,score in zip(names, scores):
  print(f'{name:<10}{score}')