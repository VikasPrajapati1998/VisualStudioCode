"""
File: listexamples.py
---------------------
This program contains examples of using different functionality of
lists to show how you can do different list operations.
"""


def access_list_elements():
    """
    Shows an example of accessing individual elements in a list
    as well as overwriting a value.
    """
    num_list = [10, 20, 30, 40, 50]
    print('num_list =', num_list)  # print list normally
    print('num_list[0] =', num_list[0])  # print 0th element of list
    print('num_list[1] =', num_list[1])  # print 1st element of list
    print('Setting num_list[0] to 15')
    num_list[0] = 15  # put 15 at 0th position of list
    print('num_list =', num_list)  # print updated list


def print_individual_list_elements():
    """
    Shows an example of using a for-loop with range to iterate
    through the elements of a list.
    """
    letters = ['a', 'b', 'c', 'd', 'e']
    print('letters =', letters)
    print('length of letters =', len(letters))
    for i in range(len(letters)):
        print(i, "->", letters[i])


def appending_elements():
    """
    Shows two examples of using appending elements onto lists.
    """
    alist = [10, 20, 30]
    print('alist =', alist)
    print('Appending 40 to alist')
    alist.append(40)
    print('Appending 50 to alist')
    alist.append(50)
    print('alist =', alist)

    new_list = []
    print('new_list =', new_list)
    print('Appending a to new_list')
    new_list.append('a')
    print('Appending 4.3 to new_list')
    new_list.append(4.3)
    print('new_list =', new_list)


def popping_elements():
    """
    Shows an example of popping elements off a list.
    """
    alist = [10, 20, 30, 40, 50]
    print('alist =', alist)
    x = alist.pop()
    print('popped element from alist, got', x)
    print('alist =', alist)
    x = alist.pop()
    print('popped element from alist, got', x)
    print('alist =', alist)
    x = alist.pop()
    print('popped element from alist, got', x)
    print('alist =', alist)
    x = alist.pop()
    print('popped element from alist, got', x)
    print('alist =', alist)
    x = alist.pop()
    print('popped element from alist, got', x)
    print('alist =', alist)


def look_up_elements():
    """
    Shows an example of using 'in' to check if a value is contained in
    a list.
    """
    str_list = ['Ruth', 'John', 'Sonia']
    print('str_list =', str_list)
    if 'Sonia' in str_list:
        print('Sonia is in str_list')


def for_each_loop():
    """
    Shows an example of using a for-each loop with a list.
    """
    str_list = ['Ruth', 'John', 'Sonia']
    for elem in str_list:
        print(elem)


def main():
    """
    We call a number of different functions that show the results
    of different list operations to show examples of how they work.
    """
    access_list_elements()
    print_individual_list_elements()
    appending_elements()
    popping_elements()
    look_up_elements()
    for_each_loop()


if __name__ == '__main__':
    main()
