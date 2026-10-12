#Given a list of strings, remove any empty strings or None values from it.

str_list = ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

new_list = list(filter(None,str_list))
print(new_list)