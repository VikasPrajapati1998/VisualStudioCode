"""_summary_ : A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.
"""
import sys, random, operator

# --------------------------------------------------------------
def count_vowels(string):
    try:
        count = 0
        for char in str.lower(string):
            if char in "aeiou":
                count += 1
        return count
    
    except Exception as e:
        print("count_vowels error : ", e)
# --------------------------------------------------------------


# ==============================================================
def main(*args):
    try:
        string = input("Enter a string : ")
        number_of_vowels = count_vowels(string)
        print("Number of vowels : ", number_of_vowels)
    
    except Exception as e:
        print("main error : ", e)
# ==============================================================


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()


