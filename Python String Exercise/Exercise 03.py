#Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1.

s1 = 'Ault' 
s2 = 'Kelly'

n = len(s1)//2
new_string = s1[:n] + s2 + s1[n:]
print(new_string)