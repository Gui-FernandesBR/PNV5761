Problema 07
===========

Enunciado
---------

Um problema de grande importância em diversos tipos de empresas é a perda de material resultante do corte de bobinas de papel, rolos de tecidos, bobinas metálicas etc.
As lâminas das máquinas de corte podem ser ajustadas para que as bobinas sejam cortadas em **diversas tiras de larguras especificadas**.

Considerem o caso de uma empresa que dispões de duas máquinas de corte:

- a máquina A para bobinas de 100 polegadas de largura e
- a máquina B para bobinas de 80 polegadas de largura.

A empresa precisa executar um programa de corte para obter:

- 600 bobinas de 60 polegadas de largura;
- 800 bobinas de 45 polegadas de largura,
- 350 bobinas de 35 polegadas de largura e
- 1200 de 25 polegadas de largura.

Admitir que toda a sobra será inutilizada;

O custo para a empresa de:

- uma bobina de 100 polegadas é R$ 1.350,00 e
- o de uma bobina de 80 polegadas é R$ 1.200,00.

Modelar o problema.

Resolução
---------

Vamos assumir que todas as bobinas possuem o mesmo comprimento, somente precisamos cortar as bobinas em tiras de larguras especificadas.

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

- :math:`x_{j}`: quantidade de conjuntos a serem cortados do padrão `j`

Antes do exercício começar, precisamos definir todos os tipos de padrão de corte possíveis de modo que possam atender às dimensões solicitadas.
Esse processamento está feito em um excel anexo a este arquivo.
Mas não há muito segredo, temos que determinar padrões para máquina A e máquina B.
No meu caso, eu consegui propor 13 padrões para a máquina A e 10 padrões para a máquina B, totalizando 23 padrões.


Demais variáveis
^^^^^^^^^^^^^^^^

- :math:`c_{a}`: custo de uma bobina de 100 polegadas;	
- :math:`c_{b}`: custo de uma bobina de 80 polegadas.


Função Objetivo
^^^^^^^^^^^^^^^

Queremos minimizar o custo.

.. math::

    \text{min} \quad C_{A} + C_{B}

Restrições
^^^^^^^^^^

Demanda:

#. Devemos produzir ao menos 600 bobinas de 60 polegadas:

    .. math::

        x_{1} + x_{2} + x_{3} + x_{14} \geq 600

#. Devemos produzir ao menos 800 bobinas de 45 polegadas:

    .. math::

        x_{4} + x_{5} + x_{6} + 2 \cdot x_{10} + x_{15} + x_{16} + x_{23} \geq 800

#. Devemos produzir ao menos 350 bobinas de 35 polegadas:
    
    .. math::

        x_{1} + x_{4} + x_{7} + x_{8} + 2\cdot x_{11} + x_{15} + x_{17} + x_{18} + 2 \cdot x_{19} \geq 350

#. Devemos produzir ao menos 1200 bobinas de 25 polegadas:

    .. math::

        x_{2} + x_{5} + x_{7} + x_{9} + 2\cdot x_{12} + 3\cdot x_{13} + x_{16} + x_{17} + x_{19} + 2\cdot x_{20} + 3\cdot x_{21} \geq 1200


Custos

#. Custo da maquina A:

    .. math::

        1350 \cdot \sum_{j=1}^{13} x_{j}

#. Custo da maquina B:

    .. math::

        1200 \cdot \sum_{j=14}^{23} x_{j}

