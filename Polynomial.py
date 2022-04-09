from typing import List, Tuple, Union

from Complex import Complex
from Matrix import Matrix
from Tools import cache


class Polynomial(object):
    precision = 11

    def __init__(self, coef: Union[List[Union[Complex, float]], Tuple[Union[Complex, float]]]):
        while len(coef) > 1 and coef[-1] == Complex(0, 0):
            coef.pop(-1)
        self.coef = tuple(coef)

    def __sub__(self, other: 'Polynomial') -> 'Polynomial':
        return Polynomial([((self.coef[i] if len(self.coef) > i else Complex(0, 0)) -
                            (other.coef[i] if len(other.coef) > i else Complex(0, 0)))
                           for i in range(0, max([len(f.coef) for f in [self, other]]))]).remove_trailing()

    def __mul__(self, other):
        return Polynomial([coef * other for coef in self.coef])

    def __rmul__(self, other):
        return Polynomial([coef * other for coef in self.coef])

    def __floordiv__(self, other: 'Polynomial') -> 'Polynomial':
        temp = self.remove_trailing()
        denom = other.remove_trailing()
        ans = [Complex(0, 0)] * (len(temp.coef))
        while len(temp.coef) >= len(denom.coef) and len(temp.coef) > 1:
            i = len(temp.coef) - len(denom.coef)
            ans[i] = (temp.coef[-1] / denom.coef[-1])
            temp -= Polynomial([Complex(0, 0)] * i + [ans[i] * x for x in denom.coef])
        return Polynomial(ans).remove_trailing()

    def __truediv__(self, other):
        return Polynomial([coef / other for coef in self.coef])

    def __rtruediv__(self, other):
        return Polynomial([coef / other for coef in self.coef])

    def __call__(self, x: Complex):
        return sum([self.coef[i] * x ** i for i in range(len(self.coef))])

    def __str__(self):
        return " + ".join(f"{self.coef[i]}x^{i}" for i in range(0, len(self.coef))[::-1])

    def __hash__(self):
        return hash(self.coef)

    @cache
    def derivative(self):
        return Polynomial([i * self.coef[i] for i in range(1, len(self.coef))]).remove_trailing()

    @cache
    def get_roots(self) -> Tuple[Complex]:
        if len(self.coef) <= 1:
            return tuple()
        if self.coef[0] == Complex(0, 0):
            return tuple([1]) + (self // Polynomial([0, 0])).get_roots()
        x = Complex(0, 1)
        while any(self.derivative()(pos).truncate(Polynomial.precision) == 0 for pos in [x, x.get_real()]):
            x += 1
        while self(x).truncate(Polynomial.precision) != 0:
            x -= self(x) / self.derivative()(x)
        multiplicity = 1
        next = self // Polynomial([-x, 1])
        deriv = self.derivative()
        while (deriv(x).truncate(Polynomial.precision) == 0):
            multiplicity += 1
            next = next // Polynomial([-x, 1])
            deriv = deriv.derivative()
        return tuple([x] * multiplicity) + next.get_roots()

    def get_root_matrix(self) -> Matrix:
        roots = self.get_roots()
        return Matrix([[root ** n for root in roots] for n in range(len(roots))])

    def remove_trailing(self):
        coef = list(self.coef)
        while len(coef) > 1 and coef[-1] == 0:
            coef.pop(-1)
        return Polynomial(coef)
