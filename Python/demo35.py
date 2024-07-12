import operator

def main(*args: tuple) -> None:
    try:
        students = {554: 'Ajay', 350: 'Ramesh', 395: 'Rakesh', 120: 'Vijay', 210: 'Mukesh', 448: 'Shubham'}
        rollno = int(input('Enter roll number : '))
        name = students.get(rollno, 'Student')
        print(f'Congratulations {name}!')
        rollno = int(input('Enter roll number : '))
        name = students.get(rollno, 'Student')
        print(f'Congratulations {name}!')

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()



