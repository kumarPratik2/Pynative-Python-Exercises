#Check if a given URL starts with “https” and ends with “.com”.

url = input('Enter URL :').lower().strip()
if url.startswith('https')and url.endswith('.com'):
  print('Is valid URL: True')
else:
  print('Is valid URL: False')