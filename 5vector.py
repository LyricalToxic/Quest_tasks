class Vector:
    def __init__(self, value_x=0, value_y=0):
        self.__x = value_x
        self.__y = value_y

    def set(self, value_x, value_y):
        self.__x = value_x
        self.__y = value_y

    def set_y(self, value_y):
        self.__y = value_y

    def set_x(self, value_x):
        self.__x = value_x

    # def __repr__(self):
    #     return "({0}, {1})".format(str(self.__x), str(self.__y))

    def print_vector(self):
        print("({0}, {1})".format(str(self.__x), str(self.__y)))

    # def __add__(self, other):
    #     return self.__x + other.__x, self.__y + other.__y

    def add(self, other):
        self.__x += other.__x
        self.__y += other.__y

    # def __sub__(self, other):
    #     return self.__x - other.__x, self.__y - other.__y

    def sub(self, other):
        self.__x -= other.__x
        self.__y -= other.__y

    # def __mul__(self, other):
    #     if isinstance(other, int) or isinstance(other, float):
    #         return self.__x * other, self.__y * other
    #     else:
    #         raise Exception("Vector can only be multiplied by a number")

    def mul(self, number):
        self.__x *= number
        self.__y *= number


v1 = Vector()
v2 = Vector(33, 19)
v1.set(12, 11)
v1.sub(v2)
v1.print_vector()
v2.print_vector()
v1.add(v2)
v1.print_vector()
v2.print_vector()