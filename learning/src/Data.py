class Data:
    def __init__(self, x, y):
        self.__private_x = x
        self.__private_y = y

    def get_x(self):
        return self.__private_x

    x = property(get_x)

    def get_y(self):
        return self.__private_y

    y = property(get_y)

    def __str__(self):
        return f"({self.get_x()}, {self.get_y()})"
