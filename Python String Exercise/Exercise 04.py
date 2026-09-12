#Given two strings, s1 and s2, create a new string from the first, middle, and last characters of each input string.

s1 = 'America' 
s2 = 'Japan'

x = len(s1)//2
y = len(s2)//2

new_string = s1[0] + s2[0] + s1[x] + s2[y] + s1[-1] + s2[-1] 
print(new_string)