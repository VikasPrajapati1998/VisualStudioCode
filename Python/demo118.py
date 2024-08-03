
# ///////////////////////////////////////////////////////////////////////////////
import json

def encode_complex(c):
    if isinstance(c , Complex):
        return (c.real, c.imag)
    else:
        raise TypeError("Complex object is not JSON serializable.")


def decode_complex(dct):
    if "__Complex__" in dct:
        return Complex(dct['real'], dct['imag'])
    return dct


class Complex:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
    
    def printData(self):
        print(self.real, self.imag)


def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        
        lst_complex = [Complex(1.0, 2.0), 
                       Complex(1.5, 0.6), 
                       Complex(2.7, 1.8), 
                       Complex(3.6, 2.9),
                       Complex(4.2, 2.2),
                       Complex(5.6, 3.4),
                       Complex(6.8, 2.9),
                       Complex(7.8, 3.8)]
        
        file = open(path+'text15.txt', 'w+')
        for complex in lst_complex:
            json.dump(complex, file, default=encode_complex)
            file.write('\n')
        file.seek(0)
        
        file.close()
        
    except Exception as e:
        print("main errro :", e)



if __name__ == "__main__":
    main()
