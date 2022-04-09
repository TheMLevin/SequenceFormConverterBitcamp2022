from typing import Tuple, List, Any

from Complex import Complex
from Tools import cache


class Matrix(object):
    def __init__(self, elements: List[List[Complex]]):
        self.elements = tuple([tuple(row) for row in elements])

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if len(self.elements[0]) == len(other.elements):
            return Matrix([[sum([self.elements[row][x] * other.elements[x][col] for x in range(len(self.elements[0]))]) for col in range(len(other.elements[0]))] for row in range(len(self.elements))])
        else:
            raise Exception("Matrix dimensions do not match")

    def __str__(self):
        return "\n".join([str([str(x) for x in row]) for row in self.elements])

    def __hash__(self):
        return hash(self.elements)

    @cache
    def complement(self, row: int, col: int) -> 'Matrix':
        return Matrix([[1]] if len(self.elements) <= 1 or len(self.elements[0]) < 1 else
                      [[self.elements[i][j] for j in range(len(self.elements[0])) if j != col]
                       for i in range(len(self.elements)) if i != row])

    @cache
    def det(self) -> Complex:
        if len(self.elements) == len(self.elements[0]):
            return self.elements[0][0] if len(self.elements) == 1\
                else sum([((-1) ** row) * self.elements[row][0] * self.complement(row, 0).det()
                          for row in range(len(self.elements))])
        else:
            raise Exception("Matrix must be square to get determinant")

    def inverse(self) -> 'Matrix':
        if len(self.elements) == len(self.elements[0]):
            return Matrix([[((-1) ** (row + col)) * self.complement(col, row).det() / self.det() for col in range(len(self.elements[0]))]
                           for row in range(len(self.elements))])
        else:
            raise Exception("Matrix must be square to invert")

    def get_col(self, col) -> Tuple[Any]:
        return tuple([row[col] for row in self.elements])