2ª QUESTÃO
==========

João é fiel comprador de um modelo tradicional de automóvel, com pouquíssimas modificações de um ano para outro, e é muito metódico.
Assim, ele consegue fazer boas previsões das despesas anuais de manutenção e do preço de revenda do carro em função do tempo de uso.
É importante destacar que João somente compra carro novo.
João tem hoje um carro com exatamente 2 anos de uso e deseja programar as aquisições e revendas de carro para os próximos 10 anos.
Proponha um modelo matemático para ajudar João a resolver seu problema.

Observação: Como você vai trabalhar com fluxo de dinheiro ao longo do tempo, admita que todas as cifras referentes a despesas ou receitas futuras já estejam referenciadas ao valor presente.


Resolução
---------

Vamos assumir que João pode comprar ou vender um carro em qualquer mês do ano, sempre ao início do mês.
Em 10 anos, haverá 120 meses, ou seja, 120 instantes em que João pode comprar ou vender um carro.

Também não queremos que João fique sem carro, então ele sempre terá um carro em mãos.
Bem como não queremos que João tenha mais de um carro em mãos, ainda que isso possa vir a ser vantajoso em termos financeiros em algum mês, isso não é prático e queremos evitar.

Notação
^^^^^^^

- :math:`t` é o índice do mês, com :math:`t = 1, 2, \ldots, 120`.
- :math:`Ca_t` é o custo de aquisição de um carro no mês :math:`t`. Esse custo supomos conhecido por João e representa o preço de um carro de mesma categoria no mês :math:`t`.
- :math:`Pr_t` é o preço de revenda de um carro no mês :math:`t`. Esse será o preço pelo qual conseguimos vender um carro usado no mês :math:`t`.
- :math:`Cm_t` é o custo de manutenção e depreciação de um carro no mês :math:`t`.
- :math:`Cf_t` é o custo fixo de manter um carro por mês. Estamos supondo que este custo já é previamente conhecido por João.
  
Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

- :math:`x_t` é uma variável binária que indica se João comprou um carro no início do mês :math:`t` ou não. Se :math:`x_t = 1`, João comprou um carro no mês :math:`t`. Se :math:`x_t = 0`, João não comprou um carro no mês :math:`t`.
- :math:`y_t` é uma variável binária que indica se João vendeu um carro no início do mês :math:`t` ou não. Se :math:`y_t = 1`, João vendeu um carro no mês :math:`t`. Se :math:`y_t = 0`, João não vendeu um carro no mês :math:`t`.

.. Veremos ao longo do exercício que as duas variáveis são redundantes entre si, ou seja, poderíamos ter apenas uma delas e o modelo seria equivalente.
.. Contudo, para fins de clareza, vamos manter as duas variáveis por enquanto.


Função objetivo
^^^^^^^^^^^^^^^

Queremos maximizar o lucro total de João ao longo dos 120 meses.
O lucro será a diferença entre o somatório de revendas e o somatório de custos.
Assim:

.. math::

   \max \sum_{t=1}^{120} \left( Pr_t \cdot y_t - Ca_t \cdot x_t - Cm_t - Cf_t \right)

Aqui vale notar que a hipótese de que João compra sempre um carro de modelo similar é exatamente importante, pois estamos desconsiderando que João sempre poderá optar por diferentes modelos de carro e que isso impacta drasticamente os custos e preços.

Restrições
^^^^^^^^^^

#. João não pode comprar um carro no início do mês 1, pois ele já tem um carro.

    .. math::

        x_1 = 0

#. João sempre deve ter ao menos 1 carro em mãos.

    Para qualquer mês :math:`m` entre 1 e 120, precisamos que o saldo de carros em mãos seja sempre positivo.

    .. math::

       \sum_{t=1}^{m} (1 + x_t - y_t) \geq 1, \quad \forall m \in \{1, \ldots, 120\}

    É importante notar que o número 1 no somatório é o saldo inicial de carros em mãos, que é 1.

#. João pode ter no máximo 1 carro em mãos.

    De forma similar, impomos que o saldo de carros em mãos em qualquer mês :math:`m` seja no máximo 1.

    .. math::

        \sum_{t=1}^{m} (1 + x_t - y_t) \leq 1, \quad \forall m \in \{1, \ldots, 120\}

#. Queremos impor que João permaneça com um carro ao final do 10º ano.

    Precisamos impor isso senão o modelo pode querer que João venda o carro no último mês para obter maior receita, porém não queremos corre o risco de João ficar sem carro após os 10 anos.


    .. math::

        y_{120} = 0



Espaço das variáveis
^^^^^^^^^^^^^^^^^^^^    

- :math:`t \in \{1, 2, \ldots, 120\} \subset \mathbb{N}`.
- :math:`x_t \in \{0, 1\} \forall t`.
- :math:`y_t \in \{0, 1\} \forall t`.
- :math:`m` é um índice de mês, com :math:`m = 1, 2, \ldots, 120`.
