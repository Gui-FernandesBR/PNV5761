Questão 4
=========

Problema clássico de Naval, bem legal, porém desafiador.
Essa questão trata de uma simplificação do problema.
O plano de estivagem é um problema bem mais complexo.


Enunciado
---------
Uma empresa de navegação quer programar o carregamento de um navio porta-contêineres
em uma viagem na rota costa leste da América do Sul-Europa.
O navio tem capacidade para :math:`N` contêineres dos quais :math:`N_{r}` são refrigerados.
Admitindo-se:

    - Ordenados os portos da rota, de 1 a :math:`n`;
    - São conhecidas as demandas de transporte de contêineres "dry", :math:`d_{ij}`, e refrigerados, :math:`r_{ij}`, entre 2 portos i e j, :math:`i<j`;
    - As taxas de frete para esses transportes são :math:`f_{ij}^{d}` e :math:`f_{ij}^{r}`, respectivamente.

A empresa tem ainda que utilizar o navio para realocar seus contêineres vazios.
A oferta ou demanda de contêineres vazios no porto :math:`i` da rota é representada por :math:`v_{i}`.
Se :math:`v_{i}>0`, :math:`v_{i}` representa a oferta de contêineres vazios;
em caso contrário, :math:`v_{i}` representa a demanda de contêineres vazios.
É óbvio que em cada porto, há demanda ou oferta de contêineres vazios do tipo "dry" e do tipo refrigerado.
Propor um modelo matemático para fazer a programação do carregamento do navio.

Resolução
---------

Coisas que eu não sabia: a empresa não cobra para transportar contêineres vazios.
Transportar contêineres vazios é uma necessidade de reposicionamento de contêineres.

Simbologia
^^^^^^^^^^

- :math:`N = \text{Número de contêineres}`
- :math:`N_{r} = \text{Número de contêineres refrigerados}`
- :math:`n = \text{Número de portos}`
- :math:`d_{ij} = \text{Demanda de transporte de contêineres "dry" entre os portos i e j}`
- :math:`r_{ij} = \text{Demanda de transporte de contêineres refrigerados entre os portos i e j}`
- :math:`f_{ij}^{d} = \text{Taxa de frete para transporte de contêineres "dry" entre os portos i e j}`
- :math:`f_{ij}^{r} = \text{Taxa de frete para transporte de contêineres refrigerados entre os portos i e j}`
- :math:`v_{i}^{d} = \text{Oferta ou demanda de contêineres vazios no porto i}`
- :math:`v_{i}^{r} = \text{Oferta ou demanda de contêineres refrigerados vazios no porto i}`


Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

- :math:`x_{ij}^{d} = \text{Quantidade de contêineres "dry" transportados entre os portos i e j}`
- :math:`x_{ij}^{r} = \text{Quantidade de contêineres refrigerados transportados entre os portos i e j}`
- :math:`y_{ij}^{d} = \text{Quantidade de contêineres "dry" vazios transportados entre os portos i e j}`
- :math:`y_{ij}^{r} = \text{Quantidade de contêineres refrigerados vazios transportados entre os portos i e j}`


Função objetivo
^^^^^^^^^^^^^^^

Queremos maximizar a receita obtida devido ao frete de contêineres "dry" e refrigerados. 
Lembre-se que não há custo para transportar contêineres vazios.

.. math::

    \text{min} \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \left( f_{ij}^{d} \cdot x_{ij}^{d} + f_{ij}^{r} \cdot x_{ij}^{r} \right)

Restrições
^^^^^^^^^^

#. A demanda de transporte de contêineres "dry" entre os portos i e j deve ser atendida:

    Perceba que não podemos transportar mais do que o que há de demanda.
    Deixamos uma inequação para que o modelo tenha mais flexibilidade.

    .. math::

        \sum_{i=1}^{n} x_{ij}^{d} \leq d_{ij}, \quad \forall j \quad \text{onde} \quad i < j

#. A demanda de transporte de contêineres refrigerados entre os portos i e j deve ser atendida:

    .. math::

        \sum_{i=1}^{n} x_{ij}^{r} \leq r_{ij}, \quad \forall j \quad \text{onde} \quad i < j


#. Capacidade do navio

    A quantidade total de contêineres transportados não pode exceder o numero de contêineres disponíveis, isso vale para qualquer trecho e qualquer um dos dois tipos de contêineres.

    Para cada trecho, determinar quais os contêineres que estão sendo transportados e quantos deles forem vazios.


    Determinando os contêineres transportados no trecho i-j:

    .. math::

        \sum_{i=1}^{m} \sum_{j=m+1}^{n} x_{ij}^{r} \leq N_{r}, \quad \forall m \in \{1, 2, \ldots, n-1\}

        \sum_{i=1}^{m} \sum_{j=m+1}^{m} \left( x_{ij}^{r} + y_{ij}^{r} + x_{ij}^{d} + y_{ij}^{d} \right) \leq N, \quad \forall m \in \{1, 2, \ldots, n-1\}
    

Agora a gente começa a saga para determinar as restrições de quantidade de contêineres vazios transportados.


Para os portos com oferta de contêineres vazios, devemos atender à demanda

#. Exemplo para o porto 5:

    .. math::

        y_{45}^{n} + y_{46}^{n} + ... + y_{4n}^{n} \leq v_{d}


#. A oferta (ou demanda) por contêineres "dry" vazios no porto i deve ser atendida:

    .. TODO: isso aqui funciona mesmo?

    .. math::

        \sum_{j=1}^{n} y_{ij}^{d} = v_{i}^{d}, \quad \forall i

#. A oferta (ou demanda) por contêineres refrigerados vazios no porto i deve ser atendida:

    .. math::

        \sum_{j=1}^{n} y_{ij}^{r} = v_{i}^{r}, \quad \forall i

#. A quantidade de contêineres "dry" transportados entre os portos i e j deve ser menor ou igual a quantidade de contêineres "dry" disponíveis no porto i:

    .. math::

        x_{ij}^{d} \leq v_{i}^{d}, \quad \forall i, j \quad \text{onde} \quad i < j

#. A quantidade de contêineres refrigerados transportados entre os portos i e j deve ser menor ou igual a quantidade de contêineres refrigerados disponíveis no porto i:

    .. math::

        x_{ij}^{r} \leq v_{i}^{r}, \quad \forall i, j \quad \text{onde} \quad i < j
    
