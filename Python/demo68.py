# Containership
class Department:
    def set_department(self):
        try:
            self.__id = input("Enter department id: ")
            self.__name = input("Enter department name: ")
        except Exception as e:
            print("Department.set_department error : ", e)
    
    def display_department(self):
        try:
            print("Department ID is: ", self.__id)
            print("Department Name is: ", self.__name)
        except Exception as e:
            print("Department.display_department error : ", e)


class Employee:
    def set_employee(self):
        try:
            self.__eid = input("Enter employee id: ")
            self.__ename = input("Enter employee name: ")
            self.__dobj = Department()
            self.__dobj.set_department()
        except Exception as e:
            print("Employee.set_employee error : ", e)
    
    def display_employee(self):
        try:
            print("Employee ID: ", self.__eid)
            print("Employee Name: ", self.__ename)
            self.__dobj.display_department()
        except Exception as e:
            print("Employee.display_employee error : ", e)


def main(*args):
    try:
        obj = Employee()
        obj.set_employee()
        obj.display_employee()
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()
