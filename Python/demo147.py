import zipfile
import os

os.listdir('.')
['data.zip']

data_zip = zipfile.ZipFile('Python//Files//data.zip', 'r')

# Extract a single file to current directory
data_zip.extract('Python//Files//file1.py')
'/home/terra/test/dir1/zip_extract/file1.py'

os.listdir('.')
['file1.py', 'data.zip']

 # Extract all files into a different directory
data_zip.extractall(path='extract_dir/')

os.listdir('.')
['file1.py', 'extract_dir', 'data.zip']

os.listdir('extract_dir')
['file1.py', 'file3.py', 'file2.py', 'sub_dir']

data_zip.close()


