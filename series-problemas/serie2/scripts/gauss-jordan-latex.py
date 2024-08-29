from fractions import Fraction
from prettytable import PrettyTable


def print_matrix(matrix, step):
    pt = PrettyTable()
    headers = [f"x{i+1}" for i in range(len(matrix[0]) - 1)] + ["b"]
    pt.field_names = headers

    for row in matrix:
        pt.add_row([str(value) for value in row])

    print(f"Passo {step}:")
    print(pt)
    print()


def generate_latex_tableau(matrix, step, operation):
    latex_code = f"Passo {step}: {operation}\n\n"
    latex_code += "\\[\n"
    latex_code += "\\renewcommand{\\arraystretch}{1.5}\n"
    latex_code += "\\begin{array}{|"
    latex_code += "c" * (len(matrix[0]) - 1) + ":c|}\n"
    latex_code += (
        "  "
        + " & ".join([f"x_{i+1}" for i in range(len(matrix[0]) - 1)])
        + " & b \\\\\\hline\n"
    )

    for row in matrix:
        row_str = " & ".join(
            [f"{Fraction(value).limit_denominator()}" for value in row[:-1]]
        )
        row_str += f" & {Fraction(row[-1]).limit_denominator()} \\\\\n"
        latex_code += "  " + row_str

    latex_code += "\\end{array}\n"
    latex_code += "\\]\n\n"

    return latex_code


def gauss_jordan(matrix: list[list], columns_to_normalize: list[int]):
    n = len(matrix)
    m = len(matrix[0])
    latex_steps = []

    for i, col in enumerate(columns_to_normalize):
        pivot = matrix[i][col]
        operation = f"Multiplicando linha {i+1} por {Fraction(1, pivot)} (inverso de {pivot}) para obter 1 na posição ({i+1}, {col+1})"
        matrix[i] = [Fraction(x, pivot) for x in matrix[i]]

        for j in range(n):
            if j != i:
                multiplier = matrix[j][col]
                operation += f"\nMultiplicando linha {i+1} por {multiplier} e subtraindo da linha {j+1}"
                matrix[j] = [matrix[j][k] - multiplier * matrix[i][k] for k in range(m)]

        latex_code = generate_latex_tableau(matrix, i + 1, operation)
        latex_steps.append(latex_code)
        print_matrix(matrix, i + 1)

    return matrix, latex_steps


if __name__ == "__main__":
    A = [
        [
            Fraction(4),
            Fraction(5, 6),
            Fraction(3),
            Fraction(2),
            Fraction(4),
            Fraction(29),
        ],
        [
            Fraction(-2),
            Fraction(23, 6),
            Fraction(3),
            Fraction(-2),
            Fraction(4),
            Fraction(11),
        ],
        [
            Fraction(-7, 2),
            Fraction(7),
            Fraction(6),
            Fraction(-4),
            Fraction(6),
            Fraction(18),
        ],
    ]
    columns_to_normalize = [0, 1, 2]

    _, latex_steps = gauss_jordan(A, columns_to_normalize)

    with open("latex_tableaux.txt", "w", encoding="utf-8") as f:
        for step in latex_steps:
            f.write(step)
