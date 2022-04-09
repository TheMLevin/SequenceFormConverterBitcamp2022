import time
from typing import List, Tuple

from Complex import Complex
from Matrix import Matrix
from Polynomial import Polynomial


def closed_form(coefs: List[float], initials: List[float]) -> Tuple[Tuple[Complex], Tuple[Complex]]:
    function = Polynomial([Complex(-x, 0) for x in coefs][::-1] + [Complex(1, 0)])
    roots = function.get_roots()

    A = function.get_root_matrix()
    y = Matrix([[Complex(x, 0)] for x in initials])
    return (A.inverse() * y).get_col(0), roots


def generate_sequence(coefs: List[int], initials: List[int], n: int):
    seq = closed_form(coefs, initials)
    return " + ".join([f"({coef})({root})^n" for coef, root in zip(*seq)]) + " =\n" + str([str(sum([seq[0][x] * seq[1][x] ** t for x in range(len(seq[0]))])) for t in range(n)])


def get_coefs() -> List[float]:
    print("Enter the term coefficients (q to finish):")
    time.sleep(.5)
    print("a_n = ")
    new_coef = input("a_(n-1) * ")
    coef = []
    while True:
        try:
            coef.append(float(new_coef))
            new_coef = input(f"+ a_(n-{1 + len(coef)}) * ")
        except ValueError:
            break

    while len(coef) > 1 and coef[-1] == Complex(0, 0):
        coef.pop(-1)

    print(f"a_n = {' + '.join([f'{x}a_(n-{i + 1})' for i, x in enumerate(coef)])}")
    return coef


def get_initials(terms: int) -> List[float]:
    print("Enter the starting values (The number of starting values is determined by the number of coefficients)")
    try:
        return [float(input(f"a_{i} = ")) for i in range(terms)]
    except ValueError:
        print("Starting values have to be numbers")
        return []


def get_num() -> int:
    n = input("How many iterations should we evaluate? ")
    try:
        return int(n)
    except ValueError:
        return -1


def define_seq() -> Tuple[List, List, int]:
    coefs = get_coefs()
    if coefs:
        time.sleep(.5)
        initials = get_initials(len(coefs))
        if initials:
            n = get_num()
            if n >= 0:
                return coefs, initials, n
            else:
                print("Num iterations must be an integer of at least 0")
                return tuple()
        else:
            return tuple()
    else:
        print("You have entered no coefs")
        return tuple()


def main():
    print("Define a recursive sequence:")
    time.sleep(.5)
    while True:
        recur = define_seq()
        if recur:
            print("Closed form:\n" + generate_sequence(*recur))
        time.sleep(.5)
        if input("Define another? (Y/N): ").upper() != 'Y':
            break


if __name__ == "__main__":
    main()
