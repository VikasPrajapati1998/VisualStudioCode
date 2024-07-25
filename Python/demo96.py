# =====================================================================================================
class InsufficientBalance(Exception):
    def __init__(self, accno, cb):
        self.__accno = accno
        self.__curbal = cb
    
    def get_details(self):
        return {'Acc no': self.__accno, 
                'Current Balance': self.__curbal}
# =====================================================================================================

# =====================================================================================================
class Customers:
    def __init__(self):
        self.__dct = {}
    
    def append(self, accno, n, bal):
        self.__dct[accno] = {'Name': n, 'Balance': bal}
    
    def deposit(self, accno, amt):
        d = self.__dct[accno]
        d['Balance'] += amt
        self.__dct[accno] = d
    
    def display(self):
        for k, v in self.__dct.items():
            print(k, v)
        print()
    
    def withdraw(self, accno, amt):
        d = self.__dct[accno]
        curbal = d['Balance']
        if curbal - amt < 5000:
            raise InsufficientBalance(accno, curbal)
        else:
            d['Balance'] -= amt
            self.__dct[accno] = d
# =====================================================================================================

def main(*args):
    try:
        c = Customers()
        c.append(123, "Sanjay", 9000)
        c.append(101, "Sameer", 8000)
        c.append(423, "Arjun", 7000)
        c.append(133, "Sanket", 6000)
        c.append(420, "Gaurav", 5000)
        c.display()   
        
        c.deposit(123, 1000)
        c.deposit(423, 2000)
        c.deposit(420, 1500)
        c.display()  
        
        try:
            c.withdraw(423, 3000)
            print("Amount withdrawn successfully")
            c.display()
            
            c.withdraw(101, 5000)
            print("Amount withdrawn successfully.")
            c.display()
        
        except InsufficientBalance as ibe:
            print("Withdrawal denied.")
            print("Insufficient Balance Error : ", ibe.get_details()) 
            print(ibe.args)  
    
    except Exception as e:
        print("main error : ", e)
    
    else:
        print("No Error found.")
    
    finally:
        print("Program end.")
        


if __name__ == "__main__":
    main()

