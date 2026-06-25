class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def parameter(self):
        return self.side * 4

    @area.setter
    def area(self, square_area):
        self.side = square_area ** (1/2)

    @parameter.setter
    def parameter(self, square_parameter):
        self.side = square_parameter / 4
