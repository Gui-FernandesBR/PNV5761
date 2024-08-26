1ª  QUESTÃO
===========

Uma empresa fabrica um produto cujo consumo é sazonal e precisa programar sua
produção para os próximos 4 períodos em que a demanda é crescente:
:math:`d_{1} < d_{2} < d_{3} < d_{4}`.

A empresa mantém uma equipe fixa de :math:`N` operários, que dá conta da
produção nos períodos de demanda baixa; quando a demanda aumenta, a empresa
contrata mão de obra temporária.
Como se trata de um tipo de trabalho muito específico, parte da equipe fixa é
utilizada para treinamento de mão de obra temporária contratada (aprendizes).
Cada operário da equipe fixa pode treinar 3 aprendizes durante cada período.

Um operário da equipe fixa produz :math:`p` unidades por período; se deslocado
para o treinamento, ele não produz nada diretamente.
Um aprendiz durante o período de treinamento tem uma capacidade de produção
:math:`q`, que cresce em cada período subsequente de uma quantidade :math:`r`,
sem necessidade de treinamento adicional.
Cada membro da equipe temporária tem um custo :math:`a`, enquanto aprendiz, e
:math:`b` em cada período subsequente.
No fim do 4º período, toda mão de obra temporária é dispensada, com um custo
unitário :math:`c` para a empresa.
A empresa pode armazenar o produto de um período para o seguinte, a um custo
unitário :math:`f`.
O estoque inicial :math:`e_{0}`, é conhecido e o final, :math:`e_{4}`, é fixado,
a priori; há ainda um limite :math:`e_{m}`, para a capacidade de armazenamento.

Formular um modelo matemático para definir a programação de produção e
contratação da empresa.

Admita que a empresa tivesse a alternativa de adiar para o período seguinte,
:math:`(j + 1)`, a entrega de parte da demanda do período :math:`j`, concedendo,
porém, um desconto, por unidade entregue fora do prazo.
Como ficaria o modelo matemático do problema?

Resolução
---------

- :math:`e_{j}`: estoque no início do período :math:`j`.
- :math:`p`: produção de um operário da equipe fixa enquanto não está treinando.
- :math:`q + k \cdot r`: produção de um aprendiz após :math:`k` períodos após o treinamento. A produção vai crescer em uma taxa constante mesmo sem receber novos treinamentos.
- :math:`a`: custo de um aprendiz no período de treinamento.
- :math:`b`: custo de um aprendiz após o período de treinamento.
- :math:`c`: custo de demissão de um aprendiz.
- :math:`f`: custo de armazenamento de uma unidade por período.
- :math:`e_{m}`: capacidade máxima de armazenamento.
- :math:`P_{j}`: produção total da empresa no período :math:`j`.

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

- :math:`x_{j}`: quantidade de operários temporários contratados no período :math:`j`.
- :math:`d_{j}^{post}`: demanda do mês :math:`j` que será atendida somente no mês seguinte.


Restrições
^^^^^^^^^^

#. Produtividade:

    A produtividade dos funcionários fixos deve ser determinada em função da \
    quantidade de funcionários temporários contratados e da quantidade em cada \
    mês, visto que 1 funcionário fixo é sempre responsável por treinar até 3 \
    funcionários temporários e durante esse período não produz nada.

    .. math::

        Q_{j}^{fixo} = p \cdot \left[ N - \text{roundup}\left( \frac{1}{3} \cdot x_{j} \right) \right], \quad \forall j \in \{1, 2, 3, 4\}

    Note que tivemos que utilizar um operador lógico (roundup) para garantir que \
    a quantidade de funcionários fixos treinando seja o menor inteiro que \
    satisfaça a condição de que cada funcionário fixo treina até 3 funcionários. \
    Isso faz com que o modelo deixe de ser linear, então precisamos linearizar. \
    Para tal, introduzimos uma variável inteira :math:`w_{j}` e fazemos: 

    .. math::

        w_{j} \geq \frac{1}{3} \cdot x_{j}

        w_{j} - 1 \leq  \frac{1}{3} \cdot x_{j}

    Deste modo garantimos que :math:`w_{j}` é o menor inteiro que satisfaça a \
    condição de que cada funcionário fixo treina até 3 funcionários. Podemos \
    então reescrever a restrição de produtividade dos funcionários fixos como:

    .. math::

        Q_{j}^{fixo} = p \cdot \left( N - w_{j} \right), \quad \forall j \in \{1, 2, 3, 4\}

    Também podemos calcular a produtividade dos funcionários temporários, que \
    é dada pela quantidade de funcionários temporários contratados no período \
    multiplicada pela produtividade de um aprendiz após :math:`k` períodos de \
    treinamento.

    .. math::

        Q_{j}^{temp} = q \cdot x_{j} + \sum_{k=2}^{j} r \cdot x_{k}, \quad \forall j \in \{1, 2, 3, 4\} 

    Note que o fator :math:`r` somente é considerado a partir do segundo período, \
    pois no primeiro período a produtividade dos aprendizes é apenas :math:`q`. 


#. Produção

    De antemão já vamos assumir que a empresa não produzirá mais do que o necessário, \
    neste caso, já fixamos que a produção será o equivalente à soma de todas as \
    demandas dos períodos mais o balanço de estoque entre os períodos. \
    A produção varia de acordo com a quantidade de operários disponíveis e a \
    quantidade de aprendizes treinados.


    .. math::

        \sum_{j=1}^{4} P_{j} = \sum_{j=1}^{4} d_{j} + e_{4} - e_{0}


    Ademais, vamos atrelar a produção à produtividade dos funcionários fixos e \
    temporários.

    .. math::

        P_{j} = Q_{j}^{fixo} + Q_{j}^{temp}, \quad \forall j \in \{1, 2, 3, 4\}

#. Atendimento demanda em cada mês

    A demanda de cada mês deve ser atendida, seja no próprio mês ou no mês seguinte. \
    Para atender a demanda eu utilizo a produção do mês e parte do estoque disponível.

    .. math::

        d_{j} - d_{j}^{post} = P_{j} + e_{j-1} - e_{j}, \quad \forall j \in \{1, 2, 3, 4\}

    Note que não podemos atrasar a demanda do último mês, não faz sentido em termos \
    de planejamento. Então:

    .. math::

        d_{4}^{post} = 0

#. Estoque

    O estoque no início de cada período é dado pela soma do estoque do período \
    anterior com a produção excedente do período, sendo que o excedente é a \
    diferença entre a produção e a demanda atendida naquele mês.

    .. math::

        e_{j} = e_{j-1} + P_{j} - (d_{j} - d_{j-1}^{post}), \quad \forall j \in \{1, 2, 3, 4\}

    Devemos também lembrar que :math:`e_{0}` e :math:`e_{4}` são fixos e pré-determinados.

#. Capacidade máxima de armazenamento

    Em nenhum momento podemos ultrapassar a capacidade máxima de armazenamento.

    .. math::

        e_{j} \leq e_{m}, \quad \forall j \in \{1, 2, 3, 4\}

#. Número máximo de operários temporários em treinamento.

    Como conhecemos de antemão o número de operários fixos, :math:`N`, e a \
    capacidade de treinamento de cada um, podemos limitar o número de \
    funcionários temporários que podem ser contratados de uma só vez em um \
    período.

    .. math::
    
        x_{j} \leq 3 \cdot N, \quad \forall j \in \{1, 2, 3, 4\}

        
Função objetivo
^^^^^^^^^^^^^^^

Queremos minimizar os custos da empresa.
Vamos considerar os seguintes custos: demanda atendida com atraso, contratação,
estocagem, demissão de temporários, 

O custo de demissão dos temporários será a soma de todos os funcionários contratados vezes o custo de demissão.
Note que a demanda é sempre crescente, portanto não faria sentido demitir um funcionário da equipe temporária antes do último período.

Primeiro calculamos o custo de demissão dos temporários:

.. math::

    C_{d} = c \cdot \sum_{j=1}^{4} x_{j}

Em seguida podemos calcular o custo de "manutenção" desses funcionários temporários, que é o custo de se manter um funcionário temporário em um período.
Perceba que o custo varia pois o funcionário temporário passa a custar de :math:`a` para :math:`b` após o primeiro período.

.. math::

    C_{m} = \sum_{j=1}^{4} \left( a \cdot x_{j}) + b \cdot \sum_{k=2}^{j} x_{k} \right), \quad \forall j \in \{1, 2, 3, 4\}


Agora calculamos o custo de armazenamento ou estoque:

.. math::

    C_{e} = f \cdot \sum_{j=1}^{4} e_{j}

Agora, assumimos que há um custo de perda de receita por demanda atendida com atraso, que é dado por:

.. math::

    C_{atraso} = \sum_{j=1}^{4} d_{j}^{post} \cdot \text{K}

onde :math:`\text{K}` é o custo por unidade de demanda atendida com atraso.

Sendo assim, a função objetivo é:

.. math::

    \text{min} \quad C_{d} + C_{m} + C_{e} + C_{atraso}


Espaço das variáveis
^^^^^^^^^^^^^^^^^^^^

A quantidade de operários contratados é um número inteiro e positivo, portanto:

.. math::
    
    x_{j} \in \mathbb{Z}^{+}, \quad \forall j \in \{1, 2, 3, 4\}

A demanda atendida em atraso é um número real podendo ser positivo ou nulo, portanto:

.. math::

    d_{j}^{post} \in \mathbb{R}^{+}, \quad \forall j \in \{1, 2, 3, 4\}


Lembre-se que introduzimos uma variável auxiliar :math:`w_{j}` para garantir
que a quantidade de funcionários fixos treinando seja o menor inteiro que satisfaça
a condição de que cada funcionário fixo treina até 3 funcionários. Portanto:

.. math::

    w_{j} \in \mathbb{Z}^{+}, \quad \forall j \in \{1, 2, 3, 4\}

É possível comentar que existem outras formas de se garantir essa tal restrição,
eventualmente sem a necessidade de tal variável auxiliar, mas a abordagem aqui foi
satisfatórias.
