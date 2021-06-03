class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            str = ''
            row = self.width * '*'
            for i in range(self.height):
                str += row + '\n'
            return str
        else: return "Too big for picture."

    def get_amount_inside(self, shape):
        width_num = self.width // shape.width
        height_num = self.height // shape.height
        return width_num * height_num

    def __str__(self):
        return "Rectangle(width={width}, height={height})".format(width = self.width, height = self.height)

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side={side})".format(side = self.width)
