class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def __str__(self):
        return 'Rectangle(width={0}, height={1})'.format(self.width, self.height)
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            return (('*' * self.width) + '\n') * self.height
    def get_amount_inside(self, shape):
        shape_area = shape.get_area()
        parent_area = self.get_area()
        amount = 0
        while parent_area >= shape_area:
            parent_area = parent_area - shape_area
            amount += 1
        return amount

        
class Square(Rectangle):
    def __init__(self, side):
        Square.width = side
        Square.height = side
    def set_side(self, new_side):
        Square.set_height(self, new_side)
        Square.set_width(self, new_side)
    def __str__(self):
        return 'Square(side={})'.format(self.width)