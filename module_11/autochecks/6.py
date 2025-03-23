class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self.__y = value

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            return  # Ігноруємо, якщо значення не число

        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (only 0 or 1 allowed)")

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (only 0 or 1 allowed)")

    def __call__(self, value=None):
        if value is None:
            return self.coordinates.x, self.coordinates.y
        if isinstance(value, (int, float)):
            return self.coordinates.x * value, self.coordinates.y * value
        return None  # Якщо value не число, повертаємо None


# Приклад використання:
vector = Vector(Point(1, 10))

print(vector())  # (1, 10) - повертає координати
print(vector(3))  # (3, 30) - множимо вектор на 3

vector[0] = 5
vector[1] = 7
print(vector())  # (5, 7) - оновлені координати

print(vector("a"))  # None - якщо передаємо не число