import os; import shutil; from zipfile import *; from time import sleep 
print('''
****************************
Mass Extraction Tool ver 1.0
****************************
''')
file_loc = input(r'''

Please paste in a single directory to locate the zip files:
''')
extract_loc = input(r'''

Please paste in a single directory to send extracted files:
''')
os.chdir(file_loc)

extract_name = f'{file_loc} - Unzipped'
count = 0
zips = os.listdir(file_loc)

for z in zips:
    if is_zipfile(z):
        unzip = ZipFile( z , 'r')
        unzip.extractall(f'{extract_name}')
        count += 1
        unzip.close()

shutil.move(extract_name, extract_loc)

print(f'''
{count} of {len(zips)} unzipped
From:
***{file_loc}***
To:
***{extract_loc}***
Successfully !''')

sleep(7.5)
exit()

