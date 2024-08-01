6ª QUESTÃO
==========

Uma empresa precisa acondicionar caixas de mesma largura, mesma altura e
comprimentos diversos em contêineres de **20 pés de comprimento**, para exportação.
Dispondo-se as caixas com o comprimento na direção longitudinal do contêiner é
possível colocar **5 fileiras** de caixas na direção transversal;
na direção vertical, é **possível empilhar 4 caixas**.

A empresa vai exportar:

- 1200 caixas de 8.0 pés de comprimento,
- 2800 caixas de 7.0 pés de comprimento,
- 3000 caixas de 5.5 pés de comprimento e
- 4000 caixas de 3.5 pés de comprimento.

Para um melhor acondicionamento das caixas, todas as fileiras e todas as camadas,
num mesmo contêiner, devem ter o mesmo arranjo.

Apresente sua proposta para acondicionamento das caixas nos contêineres.

Resolução
---------

.. Não lembro de nenhum problema de posicionamento nas aulas. Mas acho que é parecido com o problema do corte.
.. É um problema classico de empactoamento.
.. O problema comecar com "gerar os possiveis arranjos."
.. o posicionamento no conteiner é unidimensional.
.. Podem acahar a solucao do problema no solver, optional.


Notação
^^^^^^^

- Seja :math:`i` um índice do comprimento de caixa, com :math:`i = 1, 2, 3, 4` representando caixas de 8.0, 7.0, 5.5 e 3.5 pés de comprimento, respectivamente.
- Seja :math:`j` um índice do arranjo de caixas, com :math:`j = 1, 2, ...` representando os possíveis arranjos de caixas no contêiner.
- Seja :math:`l_{i}` o comprimento da caixa de comprimento :math:`i`.


Arranjos possíveis
^^^^^^^^^^^^^^^^^^

Criaremos o vetor :math:`A = [a_{ij}]` que indica a quantidade de caixas de
comprimento :math:`i` que compõem o arranjo :math:`j`.

Vamos determinar o numero de arranjos possíveis.
Existem diversas formas de se fazer isso, vamos tentar enunciar de uma forma que
seja abstrata porém compreensível.

Pegamos o menor comprimento de caixa, que é 3.5 pés.
Dividindo 20 pés por 3.5 pés, temos que é possível colocar no máximo 5 caixas do menor comprimento sem exceder o comprimento do contêiner.
Deste modo, podemos concluir que todos os arranjos possíveis devem ter no máximo 5 caixas.

Em termos de combinatória, imaginamos 5 espaços para caixas e 5 categorias de
caixas (8.0, 7.0, 5.5, 3.5 pes ou nenhuma caixa).
O número de arranjos possíveis é o número de combinações com repetição, ou seja:

.. math::

    C_{n+r-1, r} = \binom{n+r-1}{r} = \frac{(n+r-1)!}{r!(n-1)!}

Para o nosso caso, temos que :math:`n = 5` e :math:`r = 5`, logo:

.. math::

    \binom{5+5-1}{5} = \frac{(5+5-1)!}{5!(5-1)!} = \frac{9!}{5!4!} = 126


Em outras palavras, queremos escolher 5 caixas dentre 5 categorias, podendo repetir
as categorias.
É similar ao problema de se escolher **até** 5 bolas de sorvete em uma sorveteria
com 4 sabores.
No exemplo especifico, temos 126 arranjos possíveis.

Seria possível, evidentemente, elaborar uma matriz com todas as combinações
possíveis e até mesmo verificar quais combinacoes maximizariam o espaco utilizado
no conteiner, porem isso seria desnecessário e ineficiente.
Para a sequencia do execicio, basta saber que temos 126 arranjos possíveis. 


Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

Seja :math:`x_{j}` uma variável inteira que indica a quantidade de contêineres
selecionados com o arranjo :math:`j`, com :math:`j = 1, 2, ..., 126`.


Função objetivo
^^^^^^^^^^^^^^^

Queremos minimizar o número de contêineres utilizados.

.. math::

    \min \sum_{j=1}^{126} x_{j}


Restrições
^^^^^^^^^^

#. Atendimento da demanda

    Evidentemente precisamos garantir que a demanda seja completamente atendida.

    .. tem uma equacao de demanda para cada tamanho de caixa.

    .. math::

        \sum_{j=1}^{126} a_{ij} \cdot x_{j} ...

#. Capacidade dos contêineres

    Cada contêiner tem no máximo 20m de comprimento. Assim, qualquer arranjo \
    escolhido deve ter no máximo 20m de comprimento quando soma-se o comprimento \
    de todas as caixas.

    .. math::

        \sum_{i=1}^{4} a_{ij} \cdot l_{i} \cdot x_{j} \leq 20


#. Nao queremos enviar mais do que a demanda

    Essa é uma parte bastante interessante do problema e que não pode ser ignorada.

Espaço das variáveis
^^^^^^^^^^^^^^^^^^^^

De maneira mais simples, é possivel afirmar que a variavel x deve ser sempre um numero inteiro. 

.. math::

    x \in \mathbb{N}

Entretanto, podemos restringir ainda mais o espaco dessa variavel se calcularmos a quantidade maxima de arranjos que se pode fazer com as caixas disponiveis.


