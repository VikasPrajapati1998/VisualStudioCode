"""
python -m doctest filename.py -v
"""
KOREAN = '여보, 안경 안보여'
OWL = 'Mr. Owl ate my metal worm.'
HINDI = 'कडक'
ENGLISH = 'Elephant'
def main():
    user = input('Enter a string(To see default result hit enter): ')

    if user=="":
        original = HINDI
    else:
        original = user

    print(original)

    if is_palindrome(original):
        print('Is a palindrome of length ' + str(len(original)) + ' characters')
    else:
        print('Is not a palindrome...')

def is_palindrome(s):
    normalized = normalize(s)
    rev = reverse_string(normalized)
    return normalized == rev

def normalize(s):
    normalized = ''
    for ch in s:
        if ch.isalpha():
            normalized += ch.lower() # normalized = normalized + ch.lower()
    return normalized

def reverse_string(s):
    reverse = ""
    for ch in s:
        reverse = ch + reverse
    return reverse

if __name__ == '__main__':
    main()