class Model:
    def __init__(self, name:str='', type:str='', year:int=0):
        try:
            self.__model_name = name
            self.__model_type = type
            self.__model_year = year
        except Exception as e:
            print("Model.__init__ error : ", e)
    
    def set_data(self, name:str='', type:str='', year:int=0):
        try:
            self.__model_name = name
            self.__model_type = type
            self.__model_year = year
        except Exception as e:
            print("Model.set_data error : ", e)
    
    def get_data(self):
        try:
            self.__model_name = input("Enter the name of model : ")
            self.__model_type = input("Enter the type of model : ")
            self.__model_year = int(input("Enter the model year : "))
        except Exception as e:
            print("Model.get_data error : ", e)
    
    def show_data(self):
        try:
            print(f"Model Name: {self.__model_name}, ",
                  f"Model Type: {self.__model_type}, ",
                  f"Model Year: {self.__model_year}")
        except Exception as e:
            print("Model.show_data error : ", e)

class Engine:
    def __init__(self, name:str='', type:str='', piston:int=0, power:int=0):
        try:
            self.__engine_name = name
            self.__engine_type = type
            self.__engine_piston = piston
            self.__engine_power = power
        except Exception as e:
            print("Engine.__init__ error : ", e)
    
    def set_data(self, name:str='', type:str='', piston:int=0, power:int=0):
        try:
            self.__engine_name = name
            self.__engine_type = type
            self.__engine_piston = piston
            self.__engine_power = power
        except Exception as e:
            print("Engine.set_data error : ", e)
    
    def get_data(self):
        try:
            self.__engine_name = input("Enter the name of engine : ")
            self.__engine_type = input("Enter the type of engine : ")
            self.__engine_piston = int(input("Enter the number of piston : "))
            self.__engine_power = float(input("Enter the power of engine HP : "))
        except Exception as e:
            print("Engine.get_data error : ", e)
    
    def show_data(self):
        try:
            print(f"Engine Name: {self.__engine_name}, ",
                  f"Engine Type: {self.__engine_type}, ",
                  f"Engine Piston: {self.__engine_piston}, ",
                  f"Engine Power(HP): {self.__engine_power} HP")
        except Exception as e:
            print("Model.show_data error : ", e)

class Car(Model, Engine):
    def ___init__(self, car_name:str='', company:str=''):
        try:
            Model.__init__(self)
            Engine.__init__(self)
            self.__car_name = car_name
            self.__company = company
        except Exception as e:
            print("Car.__init__ error : ", e)
    
    def set_data(self, model_name, model_type, model_year, 
                 engine_name, engine_type, engine_piston, engine_power,
                 car_name, company):
        try:
            Model.set_data(self, model_name, model_type, model_year)
            Engine.set_data(self, engine_name, engine_type, engine_piston, engine_power)
            self.__car_name = car_name
            self.__company = company
        except Exception as e:
            print("Car.set_data error : ", e)
    
    def get_data(self):
        try:
            Model.get_data(self)
            Engine.get_data(self)
            self.__car_name = input("Enter the name of car : ")
            self.__company = input("Enter the name of company : ")
        except Exception as e:
            print("Car.get_data error : ", e)
    
    def show_data(self):
        try:
            Model.show_data(self)
            Engine.show_data(self)
            print(f"Car Name: {self.__car_name}, ",
                  f"Name of Company: {self.__company}")
        except Exception as e:
            print("Car.show_data error : ", e)



# ###############################################################################################
def main(*args):
    try:
        c1 = Car()
        c1.get_data()
        print()
        c1.show_data()
        
    
    except Exception as e:
        print("main error : ", e)

# ###############################################################################################


if __name__ == "__main__":
    main()

