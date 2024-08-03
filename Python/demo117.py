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
        file = open(path+'text14.txt', 'w+')
        json.dump(Complex(1.0, 2.0), file, default=encode_complex)
        file.seek(0)
        
        data = json.load(file, object_hook=decode_complex)
        print(data)
        
        file.close()
        
    except Exception as e:
        print("main errro :", e)



if __name__ == "__main__":
    main()
