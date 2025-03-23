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
        if isinstance(value, (int, float)):  # Перевірка, чи значення є числом
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):  # Перевірка, чи значення є числом
            self.__y = value


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range (only 0 or 1 allowed)")

    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            return  # Ігноруємо спробу встановлення нечислового значення

        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range (only 0 or 1 allowed)")


# Приклад використання:
vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Встановлюємо координату x вектора 10

print(vector[0])  # 10
print(vector[1])  # 10

vector[1] = "b"  # Невірне значення (не число), тому значення не зміниться
print(vector[1])  # 10