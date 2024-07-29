Questão 2
=========


Enunciado
---------

Uma empresa de navegação precisa de um navio durante 5 anos e pode afretá-lo por
períodos múltiplos de 6 meses.
Ela sabe que haverá oscilações no mercado de frete e antevê quanto pagará pelo
afretamento do navio entre o início do semestre :math:`i` e o fim do semestre :math:`j`,
para quaisquer :math:`i=1, 2,...,10` e :math:`j=i,2,...,10`.
Estabelecer o modelo matemático para determinar a programação de afretamento do navio.


Resolução
---------

Simbologia
^^^^^^^^^^

- Admitido conhecido o valor do frete para cada semestre: :math:`c_{ij}`, :math:`i=1,2,...,10` e :math:`j=i,2,...,10`.

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^^

- :math:`x_{ij}`- binária - Se um navio é afretado do início do semestre :math:`i` até o fim do semestre :math:`j`, :math:`i=1,2,...,10` e :math:`j=i,3,...,10` (note que :math:`j \geq i`, sempre).


Função objetivo
^^^^^^^^^^^^^^^^

Minimizar o custo total de afretamento do navio durante 5 anos.

.. math::

    \min \sum_{i=1}^{10} \sum_{j=i}^{10} c_{ij} \cdot x_{ij}

Restrições
^^^^^^^^^^^

#. O navio deve ser afretado por 5 anos, ou seja, todos os 10 semestres precisam de pelo menos 1 afretamento agendado. 

    Como garantir que no semestre :math:`m` - qualquer - haja um contrato de afretamento?

    .. math::

        \sum_{i=1}^{m} \sum_{j=m}^{10} x_{ij} \geq 1, \forall m=1,2,...,10
    
    .. q: trocar o <= por um =, será que facilita a resolução? Nao se sabe.


