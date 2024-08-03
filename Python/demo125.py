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

import os, shutil

def main(*args):
    try:
        print("OS Name : ", os.name)
        print("Current Working Directory : ", os.getcwd())
        print("List of directories : ", os.listdir("."))
        print("List of directories : ", os.listdir(".."))
        print("List of directories : ", os.listdir("./Python/"))
        print()
        
        if os.path.exists("mydir"):
            print("mydir already exists")
        else:
            os.mkdir("mydir")
            print("mydir created")
        
        print(os.getcwd())
        os.chdir('mydir')
        os.makedirs('.\\directory_1\\folder_2\\file_3')
        file = open('myfile.txt', 'w')
        file.write("Having one child makes you a parent...")
        file.write("Having two you are a referee")
        file.close()
        print()
        
        stats = os.stat("myfile.txt")
        print("Size = ", stats.st_size)
        print()
        
        os.rename("myfile.txt", "yourfile.txt")
        shutil.copyfile('yourfile.txt', 'ourfile.txt')
        os.remove('yourfile.txt')
        print()
        
        curpath = os.path.abspath('.')
        os.path.join(curpath, 'yourfile')
        if os.path.isfile(curpath):
            print("yourfile file exists")
        else:
            print("yourfile file doesn\'t exist.")
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
        
    

if __name__ == "__main__":
    main()
