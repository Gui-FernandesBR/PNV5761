Problema 8
==========

Enunciado
---------

Uma empresa possui 3 fábricas de um mesmo produto a partir das quais abastece diretamente seus :math:`n` consumidores.
Um estudo indicou a necessidade da implantação de centros de distribuição como elementos intermediários no escoamento da produção entre as fábricas e os clientes;
há :math:`m` locais candidatos a receber os centros de distribuição.

A empresa opera num mercado com forte concorrência e **deve colocar seu produto a um mesmo preço em todos os clientes**.
Elaborar um modelo para localização dos centro de distribuição da empresa e definição da forma de abastecimento de clientes, conhecendo as seguintes informações:

a. :math:`d_{j}`: demanda anual de cada cliente j; 
b. :math:`cp_{i}`: custo unitário de produção na fábrica i;
c. :math:`CP_{i}`: capacidade anual de produção da fábrica i;
d. :math:`ct_{ik}`: custo unitário de transporte entre fábrica :math:`i` e eventual centro distribuição k;
e. :math:`CF_{k}`: custo fixo anual do centro de distribuição k;
f. :math:`cm_{k}`: custo unitário de manipulação do produto no centro distribuição k;
g. :math:`CM_{k}`: capacidade anual de manipulação de produtos no centro de distribuição k;
h. :math:`cd_{kj}`: custo unitário de transporte entre centro de distribuição k e cliente j.

Intervalos
^^^^^^^^^^

- (i = 1, ... , 3) fábricas
- (j = 1, ... , n) clientes
- (k = 1, ... , m) centros de distribuição



Resolução
---------

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

- :math:`x_{ik}`: quantidade de produtos enviada da fábrica :math:`i` para o eventual centro de distribuição :math:`k`;
- :math:`y_{kj}`: quantidade de produtos enviada do centro de distribuição :math:`k` para o cliente :math:`j`.
- :math:`z_{k}`: 1 se o centro de distribuição :math:`k` for instalado, 0 caso contrário.

Função Objetivo
^^^^^^^^^^^^^^^^

Queremos minimizar o custo total, que por sua vez pode ser dividido em diversos custos:

- Custo de produção

    .. math::

        \sum_{i=1}^{3} \sum_{k=1}^{m} cp_{i} \cdot x_{ik}

- Custo de transporte

    .. math::

        \sum_{i=1}^{3} \sum_{k=1}^{m} ct_{ik} \cdot x_{ik} + \sum_{k=1}^{m} \sum_{j=1}^{n} cd_{kj} \cdot y_{kj}


- Custo fixo de centro de distribuição

    .. math::

        \sum_{k=1}^{m} CF_{k} \cdot z_{k}

- Custo de manipulação do produto no CD

    .. \sum_{k=1}^{m} cm_{k} \cdot z_{k} (resposta prof)

    .. math::

        \sum_{k=1}^{m} \left( cm_{k} \cdot \sum_{j=1}^{n} y_{kj} \right)


Restrições
^^^^^^^^^^

#. Demanda anual de cada cliente :math:`j`

    .. math::

        \sum_{k=1}^{m} y_{kj} = d_{j}, \quad \forall j = 1, ..., n

    Observação, fizemos a premissa de que sempre vamos conseguir atender a demanda com o que produzimos.

#. Capacidade anual de produção da fábrica :math:`i`

    .. math::

        \sum_{k=1}^{m} x_{ik} \leq CP_{i}, \quad \forall i = 1, ..., 3

#. Capacidade anual de manipulação de produtos no centro de distribuição :math:`k`

    .. math::

        \sum_{j=1}^{n} y_{kj} \leq CM_{k}, \quad \forall k = 1, ..., m
    
    Também poderíamos escrever a mesma restrição olhando para a saída.


#. Balanco de massa do CD

    Tudo que entra, sai. No longo prazo, o CD nao é produtor nem consumidor de produtos.

    .. math::

        \sum_{i=1}^{3} x_{ik} = \sum_{j=1}^{n} y_{kj}, \quad \forall k = 1, ..., m

#. Extra: precisamos de uma restrição que vincule a movimentação do produto no centro de distribuição com a instalação do centro de distribuição.

    Se :math:`\sum_{i} x_{ik} > 0`, então :math:`z_{k} = 1`.

    Ou, alternativamente, poderíamos escrever que:

    .. math::

        \sum_{i=1}^{3} x_{ik} \leq CM_{k} \cdot z_{k}, \quad \forall k = 1, ..., m

Espaço das variáveis
^^^^^^^^^^^^^^^^^^^^

Essa é uma parte importante da resolução do problema, que o professor comumente adiciona aqui.
Neste exercício, já fizemos isso lá no início.





