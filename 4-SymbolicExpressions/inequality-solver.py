import sympy as sp
from sympy.core.sympify import SympifyError


def input_reader():
    try:
        expr1 = sp.sympify(
            input('Enter an inequality in terms of x (e.g. -x**2 + 4 < 1): '))
        return expr1
    except SympifyError as e:
        print(e)
        exit(1)


def solve_polynomial(expr, x):
    polynomial = sp.Poly(expr.lhs, x)
    return sp.solve_poly_inequality(polynomial, expr.rel_op)


def solve_univariate(expr, x):
    return sp.solve_univariate_inequality(expr, x, relational=False)


def solve_rational(expr, x):
    numer, denom = expr.lhs.as_numer_denom()
    n_poly = sp.Poly(numer)
    d_poly = sp.Poly(denom)
    relation = expr.rel_op
    return sp.solve_rational_inequalities([[((n_poly, d_poly), relation)]])


if __name__ == '__main__':
    expr = input_reader()
    x = sp.Symbol('x')
    sp.pprint(expr)
    if expr.lhs.is_polynomial():
        solution = solve_polynomial(expr, x)
    elif expr.lhs.is_rational_function():
        solution = solve_rational(expr, x)
    else:
        solution = solve_univariate(expr, x)
    sp.pprint(solution)
