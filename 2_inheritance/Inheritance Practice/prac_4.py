class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def calculate_area(self):
        pass


class Color:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def apply_color(self):
        pass


class Texture:
    def __init__(self, texture_type):
        self.texture_type = texture_type

    def get_texture_type(self):
        return self.texture_type

    def set_texture_type(self, texture_type):
        self.texture_type = texture_type


class ShapeColorTexture(Shape, Color, Texture):
    def __init__(self, name, color, texture_type):
        Shape.__init__(self, name)
        Color.__init__(self, color)
        Texture.__init__(self, texture_type)


# Create an instance of ShapeColorTexture
shape_color_texture = ShapeColorTexture("Square", "Red", "Smooth")

# Access attributes and methods
print(shape_color_texture.get_name())         # Output: Square
print(shape_color_texture.get_color())        # Output: Red
print(shape_color_texture.get_texture_type()) # Output: Smooth

shape_color_texture.calculate_area()          # Calls the calculate_area() method from the Shape class
shape_color_texture.apply_color()             # Calls the apply_color() method from the Color class
shape_color_texture.set_texture_type("Rough") # Calls the set_texture_type() method from the Texture class

print(shape_color_texture.get_texture_type()) # Output: Rough
