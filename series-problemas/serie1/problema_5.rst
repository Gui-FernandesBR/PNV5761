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
minimiza as perdas de tecido

Resolução
---------

Este é um problema bastante parecido com o problema da bobina visto em aula.
Porém Aqui a gente ja recebe os padrões de corte possíveis.

Notação
^^^^^^^

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

Função objetivo
^^^^^^^^^^^^^^^

Queremos minimizar as perdas totais de tecido:

Restrições
^^^^^^^^^^

#. Atendimento da demanda

    ... adasd 


Espaço das variáveis
^^^^^^^^^^^^^^^^^^^^

