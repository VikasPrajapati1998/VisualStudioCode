def main(*args):
    """_summary_ : Copying, Moving, and Renaming Files and Directories
    Arguments:
        args: Variable Lenght Positional Arguments
    """
    # Copying Files in Python
    import os, shutil
    
    os.makedirs("Python//path//to//file.txt")
    os.makedirs("Python//path//to//dest_dir")
    
    src = 'Python//path//to//file.txt'
    dst = 'Python//path//to//dest_dir'
    shutil.copy(src, dst)
    
    # To preserve all file metadata when copying, use shutil.copy2().
    shutil.copy2(src, dst)
    
    # Copying Directories
    shutil.copytree("data_1", "data1_backup")
    
    # Moving Files and Directories
    shutil.move("dir_1/", "backup/")
    
    # Renaming Files and Directories
    import os
    os.rename("first.zip", "first_01.zip")
    
    from pathlib import Path
    data_file = Path("data_01.txt")
    data_file.rename("data.txt")
    
    # Reading ZIP Files
    import zipfile
    with zipfile.ZipFile("data.zip", 'r') as zipobj:
        zipobj.namelist()

    with zipfile.ZipFile("Python//File//data.zip", "r") as zipobj:
        bar_info = zipobj.getinfo("sub_dir//bar.py")
        bar_info.file_size
    


if __name__ == "__main__":
    main()


    