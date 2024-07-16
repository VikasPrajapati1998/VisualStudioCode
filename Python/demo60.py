class Employee:
    def set_data(self, n:str, a:int, s:float) -> None:
        try:
            self.name = n
            self.age = a
            self.salary = s
        except Exception as e:
            print("Employee.set_data error : ", e)
    
    def show_data(self) -> None:
        try:
            print(f"Employee's Name : {self.name}",
                f"Employee's Age : {self.age}",
                f"Employee's Salary : {self.salary}",
                sep = "\n", end="\n\n")
        except Exception as e:
            print("Employee.show_data error : ", e)
    

def main(*args):
    try:
        e1 = Employee()
        e1.set_data("Arju Prajapati", 25, 40000)
        e1.show_data()
        
        e2 = Employee()
        e2.set_data("Jiya Chaturvedi", 24, 40000)
        e2.show_data()
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()
