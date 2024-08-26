Aula 07
=======

- Data: 06 de agosto de 2024.

Hoje vimos o segundo exemplo numérico de simplex

Maximizar L

    L = 5x_{1} + 4x2 + 8x3 + 6x4

Sujeito a:

    5x1 + 1x2 +  5x3 + 10x4 <=  80000
    1x1 + 4x2 + 10x3 +  5x4 <= 100000
    5x1 + 3x2 +  6x3 +  5x4 <=  60000

xj >= 0 e j in {1,2,3,4}

Passo 1: precisamos passar o problema para a forma padrão.

1) passar a função objetivo para "minimizar"

    z = -5x1 - 4x2 - 8x3 - 6x4

    ou seja, z = -L

2) cuidar das restrições (colocando variáveis de folga)

    5x1 + 1x2 + 5x3 + 10x4 + x5 = 80000
    1x1 + 4x2 + 10x3 + 5x4 + x6 = 100000
    5x1 + 3x2 + 6x3 + 5x4 + x7 = 60000

    xj >= 0 com j in {1,...,7}

Pronto, agora o problema já esta na forma padrão!!
Perceba que, além de ser uma forma padrão, nos já chegamos em uma forma canônica e que por coincidência é tbm canônica.
Ela é viável pois o sistema de equações está resolvido para x5, x6 e x7 em função de x1, x2, x3 e x4 e a função z somente depende de x1, x2, x3 e x4.

Vamos montar as tabelinhas do simplex agora...

-z | -5 | -4 | -8 | -6 |  |   |   | 0
__________________________________________
x5 |  5 |  1 | 5  | 10 | 1|   |   | 80000
x6 |  1 |  4 | 10 | 5  |  | 1 |   | 100000
x7 |  5 |  3 | 6  | 5  |  |   | 1 | 60000
     x1   x2   x3  x4   x5 x6  x7

Variáveis nao básicas: x1 = x2 = x3 = x4 = 0

Vamos olhar pela coluna do -8 pois é a coluna mais negativa. que é a coluna relativa ao x3.

Professor escolheu o pivô como sendo o numero 10.
Na linha do pivô, precisa dividir tudo pelo pivô.
Nas outras linhas, vai rolar uma substituição pesada para zerar as variáveis que precisamos.

-z | -42/10 | -8/10 |   | -2    |    |  4/5  |   | 80000
____________________________________________________________
x5 |  45/10 |   -1  |   | 75/10 | 1  | -5/10 |   | 30000
x6 |   1/10 |  4/10 | 1 | 5/10  |    |  1/10 |   | 10000
x7 |  44/10 |  6/10 |   |    2  |    | -6/10 | 1 | 0         variável básica nula
        x1      x2   x3     x4    x5     x6   x7


Solução básica viável:
- Nao básicas: x1 = x2 = x4 = x6
- Básicas: (x5 = 30000,  x3 = 10000, x7 = 0)

TABELA III da pagina 49 (escrito a mao) do PDF continuação 1 

TABELA IV (quarta solução básica viável)

A solução 4 é ótima ou nao? Sim, pois nao da pra melhorar mais.



Como se explica geometricamente uma solução básica degenerada
------------------------------------------------------------

Suponha que estamos trabalhando com duas variáveis independentes.


Soluções degeneradas vs nao degeneradas?
----------------------------------------

...

Método das duas fases
----------------------

...


