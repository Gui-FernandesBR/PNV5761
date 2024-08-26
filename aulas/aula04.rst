Aula 04
=======

Data: 16/julho/2024

Na semana passada não tivemos aula pois era feriado em SP.

Hoje na primeira parte da aula vamos falar dos problemas 10 e 11.

Além disso, na segunda parte vamos iniciar o tema de Programação Linear.


Problema de transbordo
----------------------

Tenho uma rede orientada. Professor não explicou muito sobre esse exemplo.
Esse tipo de problema será estudado no terceiro modulo da materia.


Programação Linear
------------------

A ideia da disciplina é que vamos ver a base fundamental da resolução de problemas vistos até aqui.

Até aqui, criamos modelos que possuem funções objetivo lineares em torno da variável de decisão, bem como restrições lineares.

Vamos trabalhar com variáveis inteiras, reais não negativas e binarias.

A primeira etapa será trabalhar com variáveis reais não negativas.


Forma padrão do problema de programação linear
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Na forma padrão, vamos minimizar a função objetivo

todas as variáveis sao não negativas.

todas as restrições sao equações (ao invés de inequações).


Também podemos escrever isso na forma matricial.


Definição 1:

Diz-se que x' é solução viável do problema de programação linear (PPL) na forma padrão se:
    Ax = b e x' >= 0.

"A solução ótima deve ser procurada no conjunto das soluções viáveis"


Seja F (vem de "feasible") o conjunto das soluções viáveis.

Definição 2: 

Diz-se que x* é solução viável do problema de programação linear (PPL) na forma padrão se:
    x* \in F
    cx* <= cx' para todo x' \in F

    Obs.: Note que essa definição não garante que x* seja único.

Formas alternativas de problema de programação linear
-----------------------------------------------------

Essas formas são equivalente ou correspondente à forma padrão.

caso 1 -> Problema de maximização

caso 2 -> Restrições de desigualdade: colocamos uma variável de folga ou residual, seja somando (caso de <=) ou subtraindo (caso de >=) a variável de folga.

'importante que a variável s_r mantenha a mesma assinatura da '

caso 3 -> quando uma determinada variável pode assumir valores positivos e negativos.
 - neste caso, podemos introduzir um par de variáveis substituindo essa variável.

Exemplo numérico na forma padrão
--------------------------------

Quero minimizar uma função z

minimizar z

z = -4x1 + 6x2 + 6x3 - 4x4 + (9/5)x5

subject to

     4x1 +  (5/6)x2 + 3x3 + 2x4 + 4x5 = 29
    -2x1 + (23/6)x2 + 3x3 - 2x4 + 4x5 = 11
-(7/2)x1 +      7x2 + 6x3 - 4x4 + 6x5 = 18

todo x é maior igual a 0

Vamos fazer esse problema ficar expressado em termos de x1 e x2 apenas.

Professor vai usar o método de Gauss-Jordan, porem ...

Passo 1: fazer com que x3 tenha coeficiente 1 e não apareça nas equações 2 e 3


