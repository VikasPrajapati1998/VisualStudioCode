import json


def encode_complex(c):
    if isinstance(c, Complex):
        return {"__Complex__": True, "real": c.real, "imag": c.imag}
    raise TypeError("Object of type Complex is not JSON serializable")


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

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"


# #######################################################################################################################
def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        
        lst_complex = [Complex(1.0, 2.0), 
                       Complex(1.5, 0.6),
                       Complex(2.3, 1.6), 
                       Complex(2.7, 1.8), 
                       Complex(3.6, 2.9),
                       Complex(4.2, 2.2),
                       Complex(5.6, 3.4),
                       Complex(6.8, 2.9),
                       Complex(7.8, 3.8),
                       Complex(8.2, 4.7)]
        
        with open(path + 'text17.txt', 'w') as file:
            for complex in lst_complex:
                json.dump(complex, file, default=encode_complex)
                file.write('\n')
        
        
        with open(path + 'text17.txt', 'r') as file:
            file_data = file.readlines()
            file_content = [json.loads(line, object_hook=decode_complex) for line in file_data]
            for data in file_content:
                print(data)
        # with open(path + 'text17.txt', 'r') as file:
        #     while True:
        #         line = file.readline()
        #         if line == '':
        #             break
        #         file_content = json.loads(line, object_hook=decode_complex)
        #         print(file_content)
            
            
        
    except Exception as e:
        print("main error:", e)

# #######################################################################################################################



if __name__ == "__main__":
    main()
