#Задание 1

class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        str_data = ''
        for i in range(len(self.data)):
            str_data += ' '.join(map(str, self.data[i])) + '\n'
        return str_data

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            sum_matrix.append(row)
        return sum_matrix


a = Matrix([[1, 2],
            [3, 4],
            [5, 7]])

b = Matrix([[3, 8],
            [4, 9],
            [6, 10]])

c = Matrix(a + b)
print(c)



#Задание 2

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        return self.height * 2 + 0.3

a = Coat(25)
print(a.consumption)

b = Costume(172)
print(b.consumption)


def get_total_consumption(arr):
    return sum(map(lambda x: x.consumption, arr))


print(get_total_consumption([a, b]))



#Задание 2

class Cell:
    def __init__(self, piece):
        self.piece = piece

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Only for objects of class <Cell>!')
        return Cell(self.piece + other.piece)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Only for objects of class <Cell>!')
        if self.piece < other.piece:
            raise ValueError('The second cell is bigger than the first!')
        return Cell(self.piece - other.piece)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Only for objects of class <Cell>!')
        return Cell(self.piece * other.piece)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Only for objects of class <Cell>!')
        return Cell(self.piece // other.piece)

    def make_order(self, number_pieces_row):
        return ("*" * number_pieces_row + '\n') * (self.piece // number_pieces_row) + \
               '*' * (self.piece % number_pieces_row)


# создание класса для проверки работы методов на экземпляре класса, отличного от Cell
class Class2:
    piece = 1


a = Cell(36)
b = Cell(26)
print((a + b).piece)
print((a - b).piece)
#print(a + Class2())
print(a.make_order(5))