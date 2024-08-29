import matplotlib.pyplot as plt
from fractions import Fraction
import numpy as np


def plot_2d_from_matrix(matrix, cols_var_nao_basicas):
    # Cria figura e eixo
    fig, ax = plt.subplots()

    # Define o intervalo de x
    max_value = 18
    n_pontos = 50
    x = np.linspace(0, max_value, n_pontos)

    for row in matrix:
        # Acha a equação que descreve a reta
        if row[cols_var_nao_basicas[1]] != 0:
            const_ = float(row[-1] / row[cols_var_nao_basicas[1]])
            m = -float(row[cols_var_nao_basicas[0]] / row[cols_var_nao_basicas[1]])

            # Calcula os valores de y
            y = m * x + const_

            # Plota a reta
            ax.plot(
                x,
                y,
                label=f"{Fraction(row[cols_var_nao_basicas[0]])} * x_{cols_var_nao_basicas[0] + 1} + {Fraction(row[cols_var_nao_basicas[1]])} * x_{cols_var_nao_basicas[1] + 1} = {Fraction(row[-1])}",
            )

            # Preenche a área viável, assumindo y >= mx + c
            # ax.fill_between(x, y, 0, where=(y >= 0), color="lightblue", alpha=0.3)

        else:
            # Caso especial em que a variável cols_var_nao_basicas[1] é 0
            x_value = float(row[-1] / row[cols_var_nao_basicas[0]])
            ax.axvline(
                x=x_value,
                label=f"{Fraction(row[cols_var_nao_basicas[0]])} * x = {Fraction(row[-1])}",
            )
            # ax.fill_betweenx(
            #     np.linspace(0, max_value, n_pontos),
            #     x_value,
            #     0,
            #     color="lightblue",
            #     alpha=0.3,
            # )

    # desenha a região viavel assumindo que é a região que
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

    # Plotar função objetivo
    # z = 4/3*x4 - 1.9*x5
    # x5 = (4/3*x4 - z)/1.9
    # # fazer para z = 0, 5, 10, 15, 20
    x4 = np.linspace(0, 18, 100)
    for z in [-5, 0, 5, 10]:
        x5 = (4/3*x4 - z)/1.9
        ax.plot(x4, x5, label=f"z = {z}", linestyle="--")
    

    # Configurações adicionais do gráfico
    ax.set_xlim([0, max_value])
    ax.set_ylim([0, max_value])
    ax.set_xlabel(f"x_{cols_var_nao_basicas[0] + 1}")
    ax.set_ylabel(f"x_{cols_var_nao_basicas[1] + 1}")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend()
    ax.set_title("Representação gráfica do sistema no plano 2D")

    # Exibe o gráfico
    # plt.show()
    plt.savefig("series-problemas/serie2/Q1-grafico-com-z.pdf")


if __name__ == "__main__":
    # O sistema precisa estar na forma canônica!!
    A = [
        [1, 0, 0, Fraction(16, 15), Fraction(12, 5), Fraction(48, 5)],
        [0, 1, 0, Fraction(4, 5), Fraction(24, 5), Fraction(66, 5)],
        [0, 0, 1, Fraction(-44, 45), Fraction(-16, 5), Fraction(-34, 5)],
    ]
    cols_var_nao_basicas = [3, 4]  # x4 e x5
    plot_2d_from_matrix(A, cols_var_nao_basicas)
