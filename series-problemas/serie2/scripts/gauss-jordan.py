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


def gauss_jordan(matrix: list[list], columns_to_normalize: list[int]):
    n = len(matrix)
    m = len(matrix[0])

    print_matrix(matrix, 0)

    for i, col in enumerate(columns_to_normalize):
        # Dividindo a linha pelo pivô
        pivot = matrix[i][col]
        print(
            f"Multiplicando linha {i+1} por {Fraction(1, pivot)} (inverso de {pivot}) para obter 1 na posição ({i+1}, {col+1})"
        )
        matrix[i] = [
            Fraction(x, pivot) for x in matrix[i]
        ]  # Garante que a linha seja dividida como frações

        # Zerando as outras entradas na coluna
        for j in range(n):
            if j != i:
                multiplier = matrix[j][col]
                print(
                    f"Multiplicando linha {i+1} por {multiplier} e subtraindo da linha {j+1}"
                )
                matrix[j] = [matrix[j][k] - multiplier * matrix[i][k] for k in range(m)]

        # Imprimir a matriz após cada passo
        print_matrix(matrix, i + 1)

    return matrix


if __name__ == "__main__":
    # Exemplo de uso
    # fmt: off
    # A = [
    #     [Fraction(4), Fraction(5, 6), Fraction(3), Fraction(2), Fraction(4), Fraction(29)],
    #     [Fraction(-2), Fraction(23, 6), Fraction(3), Fraction(-2), Fraction(4), Fraction(11)],
    #     [Fraction(-7, 2), Fraction(7), Fraction(6), Fraction(-4), Fraction(6), Fraction(18)],
    # ]

    A = [
        [Fraction(0,1), Fraction(-1, 4), Fraction(1, 1), Fraction(1,4),  Fraction(0,1), Fraction(-1,8), Fraction(0,1), Fraction(100,1)],
        [Fraction(0,1), Fraction(5, 1),  Fraction(0, 1), Fraction(0, 1), Fraction(1,1), Fraction(-1,2), Fraction(0,1), Fraction(380,1)],
        [Fraction(1,1), Fraction(3, 2),  Fraction(0, 1), Fraction(0, 1), Fraction(0,1), Fraction(1, 4), Fraction(0,1), Fraction(230,1)],
        [Fraction(2,1), Fraction(4, 1),  Fraction(3, 1), Fraction(0, 1), Fraction(0,1), Fraction(0, 1), Fraction(1,1), Fraction(700,1)]
    ]

    columns_to_normalize = [ # começa a contar a partir do 0
        0, # x1
        2, # x3
        4, # x5
        6, # x7
    ]

    gauss_jordan(A, columns_to_normalize)
