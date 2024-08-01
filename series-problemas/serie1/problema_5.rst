5ª QUESTÃO
==========

Uma empresa está realizando seu planejamento mensal de produção de um determinado
modelo de calça jeans masculina.

Há uma demanda :math:`d_{i}` para as partes :math:`i = 1,..., 75`, necessárias
para atender às diversas combinações de tamanho de cintura e comprimento.
Estas partes são cortadas a partir de camadas de 60 a 70 peças de tecidos, que
são dispostos nas máquinas de corte.

A empresa dispõe de um conjunto de padrões de corte (moldes), sendo que cada
padrão define a forma como as várias partes podem ser cortadas.
Cada padrão de corte :math:`m = 1, \dots, 350`, gera :math:`a_{im}` cópias da
parte :math:`i` por camada de tecido, e gera uma perda de :math:`\omega_{m}`
:math:`cm^{2}` de tecido.

Formule um modelo de programação matemática para definir um plano de corte que
minimiza as perdas de tecido.

Resolução
---------

Este é um problema bastante parecido com o problema da bobina visto em aula.
Porém aqui já sabemos de antemão quais são os padrões de corte possíveis.

Notação
^^^^^^^

- :math:`i`: índice das partes, com :math:`i = 1, 2, \dots, 75`.
- :math:`m`: índice dos padrões de corte, com :math:`m = 1, 2, \dots, 350`.

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

- :math:`x_{m}`: número de camadas de tecido cortadas com o padrão de corte :math:`m`. Essa variável é inteira e não negativa.

Função objetivo
^^^^^^^^^^^^^^^

Queremos minimizar as perdas totais de tecido:

.. math::

    \min \sum_{m=1}^{350} \omega_{m} \cdot x_{m}

Restrições
^^^^^^^^^^

#. Atendimento da demanda

    Queremos atender a demanda de todas as partes:

    .. math::

        \sum_{m=1}^{350} a_{im} \cdot x_{m} \geq d_{i}, \forall i \in \{1, 2, \dots, 75\}

