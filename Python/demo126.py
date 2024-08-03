"""
_summary_
    A. __Module Content__ :
            1. os module
            2. os.path
            3. shutil
            4. pathlib
    B. __Table of Content__ :
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

import os, shutil

def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        # path = str(os.getcwd())
        file = open(path+"numbers.txt", 'wb')
        file.write(b'12345')
        file.write(b"4321")
        file.write(b"2632")
        file.write(b"833")
        file.close()
        
        file = open(path+"numbers.txt", 'rb')
        file.seek(10, 0); print("From Start Location : ", file.tell())
        file.seek(2, 1); print("From Current Location : ", file.tell())
        file.seek(-5, 1); print("From Current Location : ", file.tell())
        file.seek(-10, 2); print(file.tell())
        file.close()
    
    except Exception as e:
        print("main error : ", e)




if __name__ == "__main__":
    main()


