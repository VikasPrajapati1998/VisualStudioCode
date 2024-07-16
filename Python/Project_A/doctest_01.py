def is_divisible(a, b):
    """
    >>> is_divisible(20, 4)
    True
    >>> is_divisible(12, 7)
    False
    >>> is_divisible(10, 10)
    True
    >>> is_divisible(10, 3)
    True
    """
    return a % b == 0

def main():
    a = int(input("Enter number a = "))
    b = int(input("Enter number b = "))
    result = is_divisible(a, b)
    print(result)

if __name__ == '__main__':
    main()

"""
To Check doctest
1. Open terminal of PyCharm
2. Give this command -
        python -m doctest leap_year.py -v
3. press enter key
"""


