"""
_summary_ : Miscellany
"""
import sys
import os

def main(*args) -> None:
    """_summary_: This is the main function of program. The program execution start from here.
    
    Args:
        *args: Variable Length Positional Arguments
    
    Returns:
        Any : It can return anything to caller function.
    """
    try:
        # Documentation Strings
        print(os.__doc__)
        print("Number of arguments received = ", len(sys.argv))
        print("Arguments received = ", str(sys.argv))
        
        
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()

