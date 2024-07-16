class Employee:
    """_summary_ : 
            Employee class to get the details of employees.
    """
    count = 0
    
    def __init__(self, name:str=None, age:int=None, salary:float=None) -> None:   # private
        """
        _summary_:
            Constructor of Employee class.
        
        Args:
            name (str, optional): _description_. Defaults to None.
            age (int, optional): _description_. Defaults to None.
            salary (float, optional): _description_. Defaults to None.
        """
        try:
            self.__name = name
            self.__age = age
            self.__salary = salary
            Employee.count += 1
        
        except Exception as e:
            print("Employee Constructor error : ", e)
        
    def set_data(self, name:str, age:int, salary:float) -> None:    # public
        """
        _summary_:
            set_data method of Employee to set the data in the object variables.

        Args:
            name (str): _description_. Defaults to None.
            age (int): _description_. Defaults to None.
            salary (float): _description_. Defaults to None.
        """
        try:
            self.__name = name
            self.__age = age
            self.__salary = salary
            
        except Exception as e:
            print("Employee.set_data error : ", e)
    
    def show_data(self) -> None:    # public
        """
        _summary_:
            show_data method of Employee to print the data in the object variables.
        
        Args:
            None
        """
        try:
            print(f"Employee's Name : {self.__name}",
                  f"Employee's Age : {self.__age}",
                  f"Employee's Salary : {self.__salary}",
                  sep = "\n", end="\n\n")
            
        except Exception as e:
            print("Employee.show_data error : ", e)
    
    def __del__(self) -> None:      # private
        """
        _summary_ : 
            Destructor of Employee class to delete the objects.
        
        Args:
            None
        """
        try:
            del self.__name
            del self.__age
            del self.__salary
            print("Object deleted.", self)
        
        except Exception as e:
            print("Employee Destructor error : ", e)
    

def main(*args):
    """
    _summary_ : 
        Program start execution from here. 
    
    Args:
        args: Variable length positional arguments. Take multiple inputs and use it.
    """
    try:
        e1 = Employee()
        e1.set_data("Arju Prajapati", 25, 40000)
        e1.show_data()
        
        e2 = Employee()
        e2.set_data("Jiya Chaturvedi", 24, 40000)
        e2.show_data()
        
        print("Count = ", Employee.count)
        print()
        
        print(vars()); print()
        print(dir()); print()
        print(vars(Employee)); print()
        print(dir(Employee)); print()
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()
