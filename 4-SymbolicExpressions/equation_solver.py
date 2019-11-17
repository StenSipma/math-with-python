import sympy as sp
from sympy.core.sympify import SympifyError


def equation_reader():
    expr1, expr2 = None, None
    try:
        expr1 = sp.sympify(input('Enter an equation: '))
        expr2 = sp.sympify(input('Enter another equation: '))
    except SympifyError as se:
        return None, se
    return expr1, expr2


if __name__ == '__main__':
    expr1, expr2 = equation_reader()
    if expr1 is None:
        print(expr2)
        exit(1)

    x, y = sp.symbols('x y')
    solution = sp.solve((expr1, expr2), dict=True)
    p = sp.plot(sp.solve(expr1, y)[0], sp.solve(expr2, y)[0], legend=True)
    print(solution)
