Questão 6
=========

Problema de designação. Professor menciona que o problema é aparentemente complicado,
mas que essa é uma questão clássica.
Precisa pensar nos dois casos: máquinas em série e máquinas em paralelo.
A formulação muda bastante dependendo do caso.

Enunciado
---------

Problema de designação para reduzir o gargalo em uma linha de produção.
Admita que haja :math:`n` homens aos quais devem ser designadas :math:`n` funções em uma linha de produção.
Se a tarefa  :math:`j`  for atribuída ao homem  :math:`i`, este poderá processar :math:`a_{ij}` itens por unidade de tempo.
O gargalo é aquele homem que na designação efetuada tem a menor produtividade.
Estabeleça um modelo de programação linear para maximizar a produção. 

Resolução
---------

A resolução desse problema depende bastante se voce considera que as maquinas estão em paralelo ou em serie.
Abaixo fiz uma resolução considerando que as maquinas estão em paralelo.
Se caso fizesse com as maquinas em serie, voce estaria enfrentando o problema do gargalo.

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

.. math::

    x_{ij} = \begin{cases} 1, & \text{se a tarefa } j \text{ for atribuída ao homem } i \\ 0, & \text{caso contrário} \end{cases}

Função objetivo
^^^^^^^^^^^^^^^

Queremos maximizar a produção total nessa linha de produção, portanto:

.. math::

    \max \sum_{i=1}^{n} \sum_{j=1}^{n} a_{ij} \cdot x_{ij}


Restrições
^^^^^^^^^^

#. Cada homem deve ser designado a uma tarefa:

    .. math::

        \sum_{j=1}^{n} x_{ij} = 1, \forall i \in \{1, 2, \ldots, n\}

#. Cada tarefa deve ser designada a um homem:

    .. math::

        \sum_{i=1}^{n} x_{ij} = 1, \forall j \in \{1, 2, \ldots, n\}

Resolução em serie:
-------------------

A produção da linha está limitada à produção da máquina mais lenta.

maximizar :math:`P_{l}` (produção maquina :math:`l`) 

.. (isso é um l de lagarto, não confundir com o número 1)

.. math::

    P_{l} \leq P_{j}, \forall j in {1, 2, ..., n}

