import math

class Figure:
    def __init__(self, name):
        self.name = name

class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__("Треугольник")
        self.a = a
        self.b = b
        self.c = c
    def Perimeter(self):
        return self.a + self.b + self.c
    def Area(self):
        p = self.Perimeter()
        return math.sqrt(self.a * self.a + self.b * self.b + self.c * self.c)

class Quadrilateral(Figure):
    def __init__(self, a, b):
        super().__init__("Четырехугольник")
        self.a = a
        self.b = b
    def Perimeter(self):
        return 2 * (self.a + self.b)
    def Area(self):
        return self.a * self.b

class Circle(Figure):
    def __init__(self, r):
        super().__init__("Круг")
        self.r = r
    def Perimeter(self):
        return 2 * math.pi * self.r
    def Area(self):
        return math.pi * self.r ** 2
if __name__ == "__main__":
    shapes = [
        Triangle(3, 4, 5),
        Quadrilateral(4, 6),
        Circle(5),
    ]
    for s in shapes:
        print(f"{s.name}: периметр = {s.Perimeter():.2f}, площадь = {s.Area():.2f}")


