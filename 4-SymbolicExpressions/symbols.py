import sympy as sp

sp.init_printing(use_unicode=True)

x, y, z = sp.symbols('x y z')
a, b, c = sp.symbols('a b c')

expr1 = a * x**2 + b * x + c
expr2 = a * y**2 + b * y + c
expr3 = a * z**2 + b * z + c

expr = expr1 + expr2 + expr3
sp.pprint(expr)
simple_expr = expr.subs({x: y - 8, z: 4 * y})
sp.pprint(simple_expr)
for sol in sp.solve(simple_expr, y):
    sp.pprint(sol.subs({a: 1, b: -5}))
    sp.plot(sol.subs({a: 1, b: -5}))
