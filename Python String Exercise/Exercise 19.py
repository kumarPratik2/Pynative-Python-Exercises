#Given two strings, s1 and s2, create a third string made of the first char of s1, then the last char of s2, Next, the second char of s1 and the second-to-last char of s2, and so on. Any left-over chars go at the end of the result.

s1 = 'Abcd'
s2 = 'Xyz123'

s2 = s2[::-1]
new =''
if len(s1) > len(s2):
  n = len(s2)
else:
  n = len(s1)
for i in range(n):
   new += s1[i] + s2[i] 
new += s1[n:] + s2[n:]
print(new)