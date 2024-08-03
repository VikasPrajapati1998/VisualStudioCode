"""_summary_
__Module Content__ :
        1. os module
        2. os.path
        3. shutil
        4. pathlib
__Table of Content__ :
        1. Retrieve file properties
        2. Create directories
        3. Match patterns in filenames
        4. Traverse directory trees
        5. Make temporary files and directories
        6. Delete files and directories
        7. Copy, Move or Rename files and directories
        8. Create and extract ZIP and TAR archives
        9. Open multiple files using the fileinput module.
"""

import os

def convert(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
    
def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert(file_info.st_size)

path = "D:\\Programs\\VisualStudioCode\\Python\\demo128.py"
print(file_size(path))