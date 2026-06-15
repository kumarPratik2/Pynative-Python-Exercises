#Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.

f = open('notes.txt' , 'w')
f.write('''Hello, this is my first note.
Python file handling is simple.
End of file.''')
f.close()