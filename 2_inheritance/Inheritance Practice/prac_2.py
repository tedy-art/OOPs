"""
Create a base class called Shape with attributes color and area, and a method called
calculate_area() that calculates and sets the area of the shape. Then create two derived
classes called Rectangle and Circle that inherit from the Shape class. Implement the
calculate_area() method in each derived class to calculate and set the area of a
rectangle and a circle, respectively. Finally, create instances of the Rectangle and
Circle classes, set their color attributes, and call the calculate_area() method on each
instance.
"""

class Shape:
    def __init__(self, color):
        self.color = color
        self.area = 0

    def calculate_area(self):
        pass

class Rectange(Shape):
    def __init__(self, color, lenght, width):
        super().__init__(color)
        self.lenght = lenght
        self.width = width

    def calculate_area(self):
        self.area = self.lenght * self.width

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        self.area = 3.14 * self.radius ** 2

rectangle = Rectange('red', 5, 10)
circle = Circle('blue', 3)

rectangle.calculate_area()
circle.calculate_area()

print(f"Rectangle color is {rectangle.color} and area of rectangle is {rectangle.area}")
print(f"Circle color is {circle.color} and area of Circle is {circle.area}")
