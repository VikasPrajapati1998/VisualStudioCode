# Regex
# /////////////////////////////////////////////////////////////////////////////////////////
"""
_summary_ : The re module offers a set of functions that allows us to search a string for a match:

_Regex Functions_ : 
    1. **findall** : Returns a list containing all matches
    2. **search** : Returns a _Match object_ if there is a match anywhere in the string.
    3. **split** : Returns a list where the string has been split at each match.
    4. **sub** : Replaces one or many matches with a string.

_Metacharacters_ : 
    1.  [] : A set of characters.
    2.  \  : Signals a special sequence. 
    3.  .  : Any character.
    4.  ^  : Starts with.
    5.  $  : Ends with.
    6.  *  : Zero or more occurrences.
    7.  +  : One or more occurrences.
    8.  ?  : Zero or One occurrences.
    9.  {} : Exactly the specified number of occurrences.
    10. |  : Either or "falls|stays"
    11. () : Capture and group

_Sets_ :
    1.  [arn]       : Returns a match where one of the specified characters (a, r, or n) is present.
    2.  [a-n]       : Returns a match for any lower case character, alphabetically between a and n.
    3.  [^arn]      : Returns a match for any character EXCEPT a, r, and n.
    4.  [0123]      : Returns a match where any of the specified digits (0, 1, 2, or 3) are present.
    5.  [0-9]       : Returns a match for any digit between 0 and 9.
    6.  [0-5][0-9]  : Returns a match for any two-digit numbers from 00 and 59.
    7.  [a-zA-Z]    : Returns a match for any character alphabetically between a and z, lower case OR upper case.
    8.  [+]         : In sets, +, *, ., |, (), $, {} has no special meaning, so [+] means: return a match for any
                      + character in the string.
    
"""
# /////////////////////////////////////////////////////////////////////////////////////////


import re


def main(*args):
    try:
        string = "The rain in Spain"
        sequence = re.search("^The.*Spain$", string)
        print(sequence)
        
        '''
        _Metacharacters_ : Metacharacters are characters with a special meaning.
            1.  [] : A set of characters.
            2.  \  : Signals a special sequence. 
            3.  .  : Any character.
            4.  ^  : Starts with.
            5.  $  : Ends with.
            6.  *  : Zero or more occurrences.
            7.  +  : One or more occurrences.
            8.  ?  : Zero or One occurrences.
            9.  {} : Exactly the specified number of occurrences.
            10. |  : Either or "falls|stays"
            11. () : Capture and group
        
        '''
        print("========================== Metacharacters =================================")
        print(string)
        sequence = re.findall("[a-e]", string)
        # Find all lower case characters alphabetically between "a" and "m".
        print(sequence)
        
        sequence = re.findall("[o-v]", string)
        print(sequence)
        
        string = "That will be 598 dollars."
        sequence = re.findall("\d", string)
        print(sequence)
        
        string  = "My roll number is 18254."
        sequence = re.findall("\d", string)
        print(sequence)
        
        string = "9161589883"
        sequence = re.findall("\d", string)
        print(sequence)
        
        string = "Arjun Prajapati"
        sequence = re.findall("Ar..n Pr.....ti", string)
        print(sequence)
        
        sequence = re.findall("^Arjun", string)
        print(sequence)
        
        sequence = re.findall("^Vikas", string)
        print(sequence)
        
        sequence = re.findall("pati$", string)
        print(sequence)
        
        sequence = re.findall("Arj.*pati", string)
        print(sequence)
        
        sequence = re.findall("Arj.*n", string)
        print("Arj.*n : ", sequence)
        
        sequence = re.findall("Arj.+n", string)
        print("Arj.+n : ", sequence)
        
        sequence = re.findall("Arj.*un", string)
        print("Arj.*un : ", sequence)
        
        sequence = re.findall("Arj.+un", string)
        print("Arj.+un : ", sequence)
        
        sequence = re.findall("Ar.?n", string)
        print("Ar.?n : ", sequence)
        
        sequence = re.findall("Arj.?n", string)
        print("Arj.?n : ", sequence)
        
        sequence = re.findall("Ar.{2}n", string)
        print("Ar.{2}n : ", sequence)
        
        string_name = "Vikas Prajapati"
        sequence = re.findall("Arjun|Vikas", string_name)
        print("Arjun|Vikas : ", sequence)
        print()
        print("===========================================================================")
        print()
        
        '''
        __Special Sequences__ : A special sequence is a \ followed by one of the characters in the list below, and has a special menaing.
            1. \d : Returns a match where the string contains digits (numbers from 0-9).
            2. \D : Returns a match where the string DOES NOT contain digits.
            3. \s : Returns a match where the string contains a white space character.
            4. \S : Returns a match where the string DOES NOT contain a white space character.
            5. \w : Returns a match where the string contains any word characters 
                    (characters from a to Z, digits from 0-9, and the underscore _ charater.)
            6. \W : Returns a match where the string DOES NOT contain any word characters.
        '''
        
        print("========================== Special Sequences ===============================")
        string = "My college roll number is 18254. I can use it for my personal identity."
        seq = re.findall("\d", string)
        print(seq)
        print()
        
        seq = re.findall("\D", string)
        print(seq)
        print()
        
        seq = re.findall("\s", string)
        print(seq)
        print()
        
        seq = re.findall("\S", string)
        print(seq)
        print()
        
        seq = re.findall("\w", string)
        print(seq)
        print()
        
        seq = re.findall("\W", string)
        print(seq)
        print()
        print("===========================================================================")
        print()
        
        
        '''
        __Sets__ : A set is a set of characters inside a pair of square brackets [] with special meaning.
            1.  [arn]       : Returns a match where one of the specified characters (a, r, or n) is present.
            2.  [a-n]       : Returns a match for any lower case character, alphabetically between a and n.
            3.  [^arn]      : Returns a match for any character EXCEPT a, r, and n.
            4.  [0123]      : Returns a match where any of the specified digits (0, 1, 2, or 3) are present.
            5.  [0-9]       : Returns a match for any digit between 0 and 9.
            6.  [0-5][0-9]  : Returns a match for any two-digit numbers from 00 and 59.
            7.  [a-zA-Z]    : Returns a match for any character alphabetically between a and z, lower case OR upper case.
            8.  [+]         : In sets, +, *, ., |, (), $, {} has no special meaning, so [+] means: return a match for any
                            + character in the string.
        '''
        print("=============================== Sets ======================================")
        string = "My name is Arjun Prajapati. My college roll number is 18254."
        seq = re.findall("[aeiou]", string)
        print(seq); print()
        
        seq = re.findall("[A-Z]", string)
        print(seq); print()
        
        sentence = "The quick brown fox jumps over the lazy dog."
        seq = re.findall("[a-z]", sentence)
        print(seq); print()
        
        seq = re.findall("[^The]", sentence)
        print(seq); print()
        
        seq = re.findall("[0123]", string)
        print(seq)
        seq = re.findall("[56789]", string)
        print(seq); print()
        
        seq = re.findall("[0-9]", string)
        print(seq)
        seq = re.findall("[1-7]", string)
        print(seq); print()
        
        seq = re.findall("[1][5-9][0-5][5][1-5]", string)
        print(seq)
        seq = re.findall("[1][5-9][0-5][1-5]", string)
        print(seq); print()
        
        seq = re.findall("[a-zA-Z]", string)
        print(seq); print()
        
        seq = re.findall("[br.*wn]", string)
        print(seq); print()  
        
        print("===========================================================================")      
    
    except Exception as e:
        print("main error : ", e)
    


if __name__ == "__main__":
    main()

