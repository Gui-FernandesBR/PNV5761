import matplotlib.pyplot as plt
from fractions import Fraction
import numpy as np


def plot_2d_from_matrix(matrix, cols_var_nao_basicas):
    # Cria figura e eixo
    fig, ax = plt.subplots()

    # Define o intervalo de x
    x = np.linspace(0, 10, 400)

    lines = []

    for row in matrix:
        if row[cols_var_nao_basicas[1]] != 0:
            const_ = float(row[-1] / row[cols_var_nao_basicas[1]])
            m = -float(row[cols_var_nao_basicas[0]] / row[cols_var_nao_basicas[1]])

            # Calcula os valores de y
            y = m * x + const_

            # Armazena a equação para encontrar a interseção
            lines.append((m, const_))

            # Plota a reta
            ax.plot(
                x,
                y,
                label=f"{Fraction(row[cols_var_nao_basicas[0]])} * x + {Fraction(row[cols_var_nao_basicas[1]])} * y = {Fraction(row[-1])}",
            )

    # # Encontrar interseções das retas
    # def line_intersection(line1, line2):
    #     m1, b1 = line1
    #     m2, b2 = line2
    #     if m1 != m2:
    #         x_intersect = (b2 - b1) / (m1 - m2)
    #         y_intersect = m1 * x_intersect + b1
    #         return x_intersect, y_intersect
    #     else:
    #         return None

    # # Calcular os pontos de interseção
    # intersections = [
    #     line_intersection(lines[0], lines[1]),
    #     line_intersection(lines[1], lines[2]),
    #     line_intersection(lines[0], lines[2]),
    # ]

    # # Adicionar os pontos onde as retas cruzam os eixos
    # intersections.append((0, lines[0][1]))
    # intersections.append((0, lines[1][1]))
    # intersections.append((0, lines[2][1]))

    # # Filtrar os pontos no primeiro quadrante
    # intersections = [
    #     point for point in intersections if point and point[0] >= 0 and point[1] >= 0
    # ]

    # print(intersections)

    # # Ordenar os pontos no sentido anti-horário
    # intersections = np.array(intersections)
    # intersections = intersections[
    #     np.argsort(np.arctan2(intersections[:, 1], intersections[:, 0]))
    # ]

    intersections = np.array([
        [4.5, 2.0],
        [0.0, 2.77],
        [0.0, 2.14],
        [6.9, 0.0],
        [8.9, 0.0],
    ])

    # Plotar a região viável
    ax.fill(
        intersections[:, 0],
        intersections[:, 1],
        "grey",
        alpha=0.5,
        label="Região viável",
    )

    # Configurações adicionais do gráfico
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_xlabel(f"x_{cols_var_nao_basicas[0] + 1}")
    ax.set_ylabel(f"x_{cols_var_nao_basicas[1] + 1}")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend()
    ax.set_title("Representação gráfica do sistema no plano 2D com região viável")

    # Exibe o gráfico
    plt.show()


if __name__ == "__main__":
    # O sistema precisa estar na forma canônica!!
    A = [
        [1, 0, 0, Fraction(16, 15), Fraction(12, 5), Fraction(48, 5)],
        [0, 1, 0, Fraction(4, 5), Fraction(24, 5), Fraction(66, 5)],
        [0, 0, 1, Fraction(-44, 45), Fraction(-16, 5), Fraction(-34, 5)],
    ]

    cols_var_nao_basicas = [3, 4]  # x4 e x5
    plot_2d_from_matrix(A, cols_var_nao_basicas)
