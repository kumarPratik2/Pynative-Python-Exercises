#Write a program that takes three names (or any words) from a user in a single input prompt and assigns them to three separate variables.

name1, name2, name3 = input('Enter three names: ').split()
print(f'First Name : {name1}')
print(f'Second Name : {name2}')
print(f'Third Name : {name3}')