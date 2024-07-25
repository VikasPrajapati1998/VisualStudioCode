from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Draw a Rectangle.")

class Circle(Shape):
    def draw(self):
        print("Draw a Circle.")
        

def main(*args):
    try:
        # s = Shape()
        r = Rectangle()
        r.draw()
        c = Circle()
        c.draw()
        print()
        
        print(isinstance(r, Shape))
        print(isinstance(c, Shape))
        print(issubclass(Rectangle, Shape))
        print(issubclass(Rectangle, object))
        print(issubclass(Circle, Shape))
        print(issubclass(Circle, object))
        print(issubclass(Rectangle, Circle))
        print(issubclass(Circle, Rectangle))
        
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()
