#Write a program to find the total count of the substring “USA” in a given string, ignoring the case (i.e., both “usa” and “USA” should be counted).

str1 = "Welcome to USA. usa awesome, isn't it?"

low = str1.lower()
counter = low.count('usa')
print(f'The USA count is: {counter}')