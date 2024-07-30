Problema 11
===========

Professor diz que este problema é análogo ao problema do caixeiro viajante, um problema clássico de otimização combinatória.

Uma das restrições mais importantes nesse problema eh a questão de se evitar sub-ciclos.
Isso porque às vezes podemos ter 2 sub-ciclos que juntos atendem todos os nos de demanda. 

Há pelo menos 2 formas de se resolver a questão dos sub-ciclos.

Enunciado
---------

Uma fábrica de tintas produz diariamente, numa mesma instalação, bateladas de tintas de :math:`n` cores diferentes.
Após cada batelada, é necessário limpar adequadamente a instalação para a produção da nova tinta;
ao fim do dia, após a última batelada, adota-se o mesmo procedimento, deixando a instalação preparada para o dia seguinte.
Admitindo conhecidos os tempos de preparação da instalação entre dois pares quaisquer de cores :math:`i` e :math:`j`, :math:`t_{ij}`, proponha um modelo matemático para a escolha da sequência diária das cores das bateladas.

Resolução
---------

Devemos minimizar o tempo total de limpeza da instalação.
Contudo, sabemos que durante a noite sempre teremos que limpar a instalação, independente da ordem das cores.

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

- :math:`x_{ij}`: variável binária que indica se a cor :math:`i` é seguida pela cor :math:`j`, ou seja, se a cor :math:`j` for fabricada logo após a cor :math:`i`.

Função Objetivo
^^^^^^^^^^^^^^^^

Queremos minimizar o tempo total de limpeza da instalação.

.. math::

    \text{min} \quad \sum_{i=1}^{n} \sum_{j=1}^{n} t_{ij} \cdot x_{ij}; \quad i \neq j



Restrições
^^^^^^^^^^

Note que com as três primeiras restrições, somente, nós ainda podemos ter sub-roteiros.  

#. Cada cor pode preceder uma única cor:

    .. math::

        \sum_{j=1}^{n} x_{ij} = 1, \quad \forall i \in \{1, 2, \ldots, n\}

#. Cada cor deve ser precedida por uma única cor:


    .. math::

        \sum_{i=1}^{n} x_{ij} = 1, \quad \forall j \in \{1, 2, \ldots, n\}

#. Demanda

    Ainda que essa restrição possa ser um pouco redundante, é válida escrevê-la aqui.
    O que queremos é garantir que todas as :math:`n` cores serão fabricadas.


    .. math::

        \sum_{j=1}^{n} \sum_{i=1}^{n} x_{ij} = n - 1

#. Evitar sub-roteiros

    Seja Q um subconjunto de cores, tal que :math:`|Q| \geq 2`.
    Vamos garantir que não haja sub-roteiros dentro de Q, para tanto:

    .. math::

        \sum_{i \in Q} \sum_{j \neq i, j \in Q} x_{ij} \leq |Q| - 1

    Essa é a formulação de Danzig, apesar de não ser a única.
