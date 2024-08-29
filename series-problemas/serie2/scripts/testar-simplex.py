import math
import numpy as np
from fractions import Fraction
from prettytable import PrettyTable

# Considere o problema na forma padrão:
# minimizar z = c*x
# sujeito a Ax = b e x >= 0


def to_tableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]


def can_be_improved(tableau):
    z = tableau[-1]
    return any(x > 0 for x in z[:-1])


def get_pivot_position(tableau):
    z = tableau[-1]
    column = next(i for i, x in enumerate(z[:-1]) if x > 0)

    restrictions = []
    for eq in tableau[:-1]:
        el = eq[column]
        if el > 0:
            restrictions.append(eq[-1] / el)
        else:
            restrictions.append(float("inf"))  # Representa uma restrição inválida

    row = restrictions.index(min(restrictions))
    return row, column


def pivot_step(tableau, pivot_position):
    new_tableau = [[] for eq in tableau]

    i, j = pivot_position
    pivot_value = tableau[i][j]
    new_tableau[i] = [x / pivot_value for x in tableau[i]]

    for eq_i, eq in enumerate(tableau):
        if eq_i != i:
            multiplier = [x * tableau[eq_i][j] for x in new_tableau[i]]
            new_tableau[eq_i] = [eq[k] - multiplier[k] for k in range(len(eq))]

    return new_tableau


def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1


def get_solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns:
        sol = 0
        if is_basic(column):
            one_index = column.tolist().index(1)
            sol = columns[-1][one_index]
        solutions.append(sol)

    return solutions


def display_tableau(tableau):
    pt = PrettyTable()
    num_vars = len(tableau[0]) - 1
    headers = [f"x{i+1}" for i in range(num_vars)] + ["b"]
    pt.field_names = headers

    for row in tableau:
        pt.add_row([str(value) for value in row])

    print(pt)


def simplex(c, A, b):
    tableau = to_tableau(c, A, b)
    print("Initial Tableau:")
    display_tableau(tableau)

    idx = 1

    while can_be_improved(tableau):
        pivot_position = get_pivot_position(tableau)
        tableau = pivot_step(tableau, pivot_position)
        print(f"Tableau {idx}:")
        display_tableau(tableau)
        idx += 1

    return get_solution(tableau)


if __name__ == "__main__":
    c = [-4, 6, 6, -4, Fraction(9, 2)]
    A = [
        [4, Fraction(5, 6), 3, Fraction(2), 4],
        [-2, Fraction(23, 6), 3, -2, 4],
        [Fraction(-7, 2), Fraction(7), 6, -4, 6],
    ]
    b = [29, 11, 18]

    solution = simplex(c, A, b)
    print("Solution:", [str(x) for x in solution])
