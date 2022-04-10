from Tools import cache


class Complex(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other) -> 'Complex':
        return Complex(self.a + other.a, self.b + other.b) if isinstance(other, Complex) else other + self

    def __radd__(self, other) -> 'Complex':
        return Complex(self.a + other, self.b)

    def __sub__(self, other) -> 'Complex':
        return Complex(self.a - other.a, self.b - other.b) if isinstance(other, Complex) else self.__rsub__(other)

    def __rsub__(self, other):
        return Complex(self.a - other, self.b)

    def __neg__(self):
        return Complex(-self.a, -self.b)

    def __mul__(self, other) -> 'Complex':
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a) if isinstance(other, Complex) else other * self

    def __rmul__(self, other):
        return Complex(self.a * other, self.b * other)

    def __truediv__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            numerator = self * other.conjugate()
            denominator = other * other.conjugate()
            return Complex(numerator.a / denominator.a, numerator.b / denominator.a)
        else:
            return self.__rtruediv__(other)

    def __rtruediv__(self, other):
        return Complex(self.a / other, self.b / other)

    @cache
    def __pow__(self, power: int) -> 'Complex':
        if not isinstance(power, int) or power < 0:
            raise TypeError("Complex exponents have only been implemented for integer powers >= 0.")
        if power == 0:
            return Complex(1, 0)
        elif power == 1:
            return self

        powers = [int(x) for x in format(power, 'b')][::-1]
        if sum(powers) == 1:
            return self ** (power // 2) * self ** (power // 2)
        else:
            prod = Complex(1, 0)
            for place in range(len(powers)):
                if powers[place]:
                    prod *= self.__pow__(2 ** place)
            return prod

    def __str__(self) -> str:
        short = self.truncate(5)
        return f"{short.a if short.a or not short.b else ''}{(' + ' if short.b > 0 else ' - ') if short.a and short.b else ''}{f'{abs(short.b)}i' if short.b else ''}"

    def __abs__(self) -> float:
        return (self.a ** 2 + self.b ** 2) ** .5

    def __eq__(self, other) -> bool:
        return self.a == other.a and self.b == other.b if isinstance(other, Complex) else self.a == other and not self.b

    def __hash__(self) -> int:
        return hash((self.a, self.b))

    def conjugate(self) -> 'Complex':
        return Complex(self.a, -self.b)

    def truncate(self, dec: int) -> 'Complex':
        return Complex(int(self.a * 10 ** dec + (.5 if self.a >= 0 else -.5)) / 10 ** dec,
                       int(self.b * 10 ** dec + (.5 if self.b >= 0 else -.5)) / 10 ** dec)

    def get_real(self) -> 'Complex':
        return Complex(self.a, 0)