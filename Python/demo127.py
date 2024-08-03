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

def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        with open(path+"text22.txt", 'w+') as file:
            while True:
                content = input("Enter the file content : ")
                if content == '':
                    break
                file.write(content)
                file.write("\n")
                
        
        with open(path+"text22.txt", 'r+') as file:
            content = file.read()
            print(content)
    
    except Exception as e:
        print("main error : ", e)
    finally:
        print()
        

if __name__ == "__main__":
    main()

