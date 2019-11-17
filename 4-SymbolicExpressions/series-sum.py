import sympy as sp
from sympy.core.sympify import SympifyError


def input_reader():
    try:
        expr1 = sp.sympify(input('Enter the n-th term of a series: '))
        n = int(input('Enter n: '))
        return expr1, n
    except (SympifyError, ValueError) as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    exp, num = input_reader()
    assert (num > 0)

    n = sp.Symbol('n')
    series = sp.summation(exp, (n, 1, num))
    sp.pprint(series)
