#Write a script that opens an existing .txt file and counts the total number of words it contains.
#sample text : Coding is the language of the future.

f = open('Sample.txt' , 'r')
text = f.read()
x = text.split()
print(len(x))