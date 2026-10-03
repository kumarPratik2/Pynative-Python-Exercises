#Given a filename as a string, extract only the file extension (e.g., .png or .pdf).

file_name = 'report_final_v2.pdf'

n = file_name.rfind('.')
extension = file_name[n+1:]
print(f'The extension used in {file_name} is: {extension}')