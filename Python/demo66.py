# This class behave like a structure in c
class Bird:
    pass

def printBird(b):
    try:
        print(f"Name: {b.name}",
            f"Weight: {b.weight}",
            f"Color: {b.color}",
            f"Animal Type: {b.animalType}",
            sep="\n", end="\n\n")
    except Exception as e:
        print("printBird error : ", e)

def main(*args):
    try:
        b = Bird()

        # Create attributes dynamically
        b.name = "Sparrow"
        b.weight = 500
        b.color = "light brown"
        b.animalType = "Vertebrate"
        printBird(b)

        # modify attributes dynamically
        b.weight = 450
        b.color = "brown"
        printBird(b)

        # delete attributes dynamically
        del b.animalType
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()
