4ª QUESTÃO
==========

Uma empresa dispõe de uma frota homogênea para fazer entrega de seus produtos a
partir de um determinado depósito.
Num dado dia, a empresa deve atender :math:`m` clientes e um "roteirista" já
identificou, preliminarmente, todos os :math:`n` roteiros viáveis
:math:`R_{1}, R_{2}, \dots R_{n}`, com custos :math:`c_{1}, c_{2}, \dots c_{n}`,
respectivamente, cada qual atendendo um certo subconjunto de clientes.

Um roteiro :math:`R_{j}` é caracterizado por um vetor
:math:`Aj = [a_{1j}, a_{2j},\dots a_{mj}]^{T}` em que :math:`a_{ij} = 1` se o
roteiro :math:`j` passa pelo cliente :math:`i` e :math:`a_{ij} = 0`, em caso contrário.
Por motivo específico, dois desses :math:`m` clientes, :math:`r` e :math:`s`
respectivamente, devem ser colocados num mesmo roteiro.

Formular o modelo matemático para determinar a melhor forma de atender os clientes.


Resolução
---------

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

Considere a variável binária :math:`x_{j}` que indica se o roteiro :math:`j` foi escolhido ou não.

Função objetivo
^^^^^^^^^^^^^^^

Queremos minimizar o custo total:

.. math::

   \min \sum_{j=1}^{n} c_{j} \cdot x_{j}, \quad \forall j \in \{1, \ldots, n\}


Restrições
^^^^^^^^^^

#. Cada cliente deve ser atendido:

    Para cada cliente, quero que o somatório de vezes em que algum roteiro passa por ele seja maior ou igual a 1.

    .. math::

       \sum_{j=1}^{n} a_{ij} \cdot x_{j} \geq 1, \quad \forall j \in \{1, \ldots, m\} 

#. Cada cliente é atendido uma única vez:

    Para cada cliente, quero que o somatório de vezes em que algum roteiro passa por ele seja menor ou igual a 1.

    .. math::

       \sum_{j=1}^{n} a_{ij} \cdot x_{j} \leq 1, \quad \forall j \in \{1, \ldots, m\}


#. Os clientes :math:`r` e :math:`s` devem ser atendidos no mesmo roteiro:

    Essa é uma complicação do modelo. Para garantir que os clientes :math:`r` e \
    :math:`s` sejam atendidos no mesmo roteiro, podemos garantir que o \
    produto dos vetores :math:`x_{j}` e :math:`a_{rj}` seja igual ao \
    produto dos vetores :math:`x_{j}` e :math:`a_{sj}`. Ou seja, para qualquer \
    roteiro escolhido, os clientes :math:`r` e :math:`s` devem ser atendidos \
    juntos.

    .. math::

       x_{j} \cdot a_{rj} = x_{j} \cdot a_{sj}, \quad \forall j \in \{1, \ldots, n\}

