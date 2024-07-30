Problema 10
===========

Enunciado
---------

Uma empresa de geração de energia elétrica fez uma projeção da demanda por energia para 5 anos futuros, em 10^6 kWh, a saber: 80, 100, 120, 140, 160.
A empresa possui 4 formas de suprir esta demanda, a partir da construção de usinas, tendo os seguintes custos e capacidades:

=====  ===========  ============  ============
Usina  Capacidade   Custo de      Custo Anual
       (10^6 kwh)   Construção    de Operação
                    (10^6 $)      (10^6 $)
=====  ===========  ============  ============
1       70           20            1.5
2       50           16            0.8
3       60           18            1.3
4       40           14            0.6
=====  ===========  ============  ============

Parte A
^^^^^^^

Formule um modelo de programação matemática para atender a demanda dos 5 anos a um custo mínimo.

Parte B
^^^^^^^

Suponha que no começo do ano 1 todas estão abertas e que a empresa gestora poderá fechar qualquer uma das usinas ao final de um ano ou abrir uma usina fechada no início de um ano, mediante os custos abaixo mostrados. Como ficaria o modelo, para atender a demanda dos 5 anos a um custo mínimo?

.. TODO: essa tabela esta saindo bem mal formatada. Testar outras formas de fazer isso.


=====  =========  ==========
Usina  Custo de   Custo de
       Re-abrir   Fechar
       (10^6 $)   (10^6 $)
=====  =========  ==========
1      1.9        1.7
2      1.5        1.2
3      1.6        1.3
4      1.1        0.8
=====  =========  ==========



Resolução
---------

Parte A
^^^^^^^

#. :math:`i` é uma variável inteira que vai de 1 a 4, representando cada usina.

#. Seja :math:`x_{ij}` uma variável binária que representa se a usina :math:`i` foi entregue para a empresa no início do ano :math:`j`. O custo de construção é lançado no ano :math:`j` (hipótese simplificadora).

#. :math:`y_{ij}` é uma variável binária que indica se a usina :math:`i` vai operar no ano :math:`j`.

Função Objetivo
***************

Temos que olhar os custos de construção e operação das usinas, assim nessa ordem:

.. math::

    min \sum_{i=1}^{4} \sum_{j=1}^{5} cc_{i} \cdot x_{ij} + \sum_{i=1}^{4} \sum_{j=1}^{5} co_{i} \cdot y_{ij}



Restrições
**********

#. Atendimento da demanda de energia em cada ano j:

    .. math::

        \sum_{i=1}^{4} cap_{i} \cdot y_{ij} \geq demanda_{j}, \quad \forall j \in \{1, 2, 3, 4, 5\}

#. A empresa não pode operar se não for entregue. Ou seja, devemos vincular x e y:

    .. math::

        y_{i1} \leq x_{i1}, \quad \forall i \in \{1, 2, 3, 4\}
        
        y_{i2} \leq x_{i1} + x_{i2}, \quad \forall i \in \{1, 2, 3, 4\}
        
        y_{i3} \leq x_{i1} + x_{i2} + x_{i3}, \quad \forall i \in \{1, 2, 3, 4\}
        
        y_{i4} \leq x_{i1} + x_{i2} + x_{i3} + x_{i4}, \quad \forall i \in \{1, 2, 3, 4\}

        y_{i5} \leq x_{i1} + x_{i2} + x_{i3} + x_{i4} + x_{i5}, \quad \forall i \in \{1, 2, 3, 4\}

ou, matematicamente:

    .. math::

        y_{ij} \leq \sum_{j=1}^{k} x_{ij}, \quad \forall i \in \{1, 2, 3, 4\}, \forall k \in \{1, 2, 3, 4, 5\}



Espaço das variáveis
********************

:math:`x_{ij}` e :math:`y_{ij}` variáveis binarias


Parte B
^^^^^^^

- :math:`w_{ij}` = 1 se a usina i é fechada no inicio do ano j
- :math:`w_{ij}` = 0 em caso contrario
- :math:`z_{ij}` = 1 se a usina i é reaberta no inicio do ano j
- :math:`z_{ij}` = 0 em caso contrario


Temos que considerar os custos de operação, fechamento e reabertura.

A expressão de custos de operação será o mesmo do item anterior.

.. math::

    min(CT), 

    CT = \sum_{i=1}^{4} \sum_{j=1}^{5} co_{i} \cdot y_{ij} + cf_{i} \cdot w_{ij} + cr_{i} \cdot zij


Agora que já temos a função objetivo, escrevemos as restrições:

.. math::

    \sum_{i=1}^{4} cap_{i} \cdot y_{ij} > demanda_{j}, 

E temos que vincular as diferentes variáveis de decisão.

.. math::

    y_{ij} = y_{i, j-1} - wij + zij, 

:math:`j` maior igual a 2, pois ela só não vale para :math:`j=1` já que não podemos reabrir uma usina no inicio do ano 1.



