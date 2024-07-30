Questão 5
=========

Essa é uma variação do problema da mochila (tendo uma mochila, como maximizar a utilidade dados os produtos que vamos colocar ali dentro).

Enunciado
---------

O gerente de publicidade de uma revista semanal precisa resolver o seguinte problema.
O número de páginas disponíveis para publicidade em cada uma das próximas semanas é :math:`n_{t}`, t = 1, 2, ..., N.
A revista recebeu pedidos de :math:`m` clientes para inserção de propaganda.
Cada pedido :math:`K` especifica:

i. a semana inicial para veiculação do anúncio, :math:`i_{K}`;
ii.	a duração em semanas da propaganda, :math:`d_{K}`;
iii. o tamanho do anúncio, :math:`a_{K}` (um quarto de página, meia página ou página inteira);
iv.	o preço oferecido :math:`p_{K}`.

a. Estabelecer um modelo matemático para selecionar os pedidos que serão aceitos;
b. Admitindo a existência de requisitos de balanceamento de propaganda tais que, se for aceito um pedido do subconjunto :math:`S_{1}`, também deverá ser aceito um pedido do subconjunto :math:`S_{2}`, que alteração haveria no modelo matemático?


Resolução
---------

Vamos ignorar o problema de empacotamento para simplificar nossa resolução.
Ou seja, não estamos preocupados em alocar os pedidos de forma a maximizar o espaço ocupado em cada semana.

a. O modelo matemático para selecionar os pedidos que serão aceitos é o seguinte:

    - Seja :math:`x_{K}` uma variável binária que indica se o pedido :math:`K` foi aceito ou não.
    - Seja :math:`i_{it}` uma variável binária que indica se o pedido :math:`K` foi aceito para inicio na semana :math:`t`.

    O objetivo é maximizar o lucro total, que é a soma dos lucros de cada pedido aceito:

    .. math::

        \max \sum_{K=1}^{m} p_{K} \cdot x_{K}
    
    Sujeito a:

    #. Cada pedido só pode ser aceito uma vez:

        .. math::

            \sum_{K=1}^{m} x_{K} \leq 1
    
    #. A duração de cada pedido aceito precisa ser respeitada:

        .. math::

            \sum_{K=1}^{m} d_{K} \cdot x_{K} \leq N - i_{Kt}, \forall t = 1, 2, ..., N
    
    #. Espaço disponivel para publicidade em cada uma das semanas do horizonte

        Perceba que os pedidos possuem duração, então precisamos considerar a duração de cada pedido aceito, para sabermos o espaço ocupado em cada semana.

        Seja :math:`b_{Kt} = 1 ` se t entre o inicio e (inicio + duração) e zero fora disso.

        Não podemos utilizar, na semana t, mais do que :math:`n_{t}` paginas para publicidade.

        .. math::

            \sum_{K=1}^{m} a_{K} \cdot b_{Kt} \cdot x_{K} \leq n_{t}, \forall t = 1, 2, ..., N

        Note que :math:`x_{K}` é uma variável binaria.

 
b. Modelo mais complicado:

    - Vamos introduzir uma variável binária :math:`y_{S1}` que indica se ao menos um pedido do subconjunto :math:`S1` foi aceito.
    - Similarmente, :math:`y_{S2}` indica se ao menos um pedido do subconjunto :math:`S2` foi aceito.

    A função objetivo é a mesma, mas agora temos mais uma restrição:

    #. Se ao menos um pedido do subconjunto :math:`S1` foi aceito, então um pedido do subconjunto :math:`S2` também deve ser aceito:

        .. math::

            y_{S1} \leq y_{S2}

