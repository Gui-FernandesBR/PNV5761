3ª QUESTÃO
==========

Uma empresa de transporte aéreo dispõe de uma frota de :math:`N_{v}` aeronaves;
a aeronave v, v = 1, 2, ..., Nv, dispõe de :math:`K_{v}` poltronas para o transporte de passageiros.
A empresa oferece um serviço sem escalas e opera voos entre m  pares de cidades (o voo entre a cidade A e a cidade B, para efeito dessa contagem, é distinto do voo entre a cidade B e a cidade A)

A empresa utiliza uma única cidade-base para sua frota e  os primeiros voos do dia de cada aeronave começam e os últimos voos do dia terminam nessa cidade;
fora essas restrições, cada aeronave pode, ao longo do dia, ser utilizada em diversos trechos da malha aérea coberta pela empresa.
Numa etapa inicial, para programar a operação da frota, foi desenvolvido um estudo que determinou, para cada avião da frota, os diversos roteiros diários viáveis, começando e terminando na cidade-base.
Cada roteiro viável :math:`j` de uma aeronave :math:`v` é identificado por um parâmetro ????? , que representa o seu custo operacional e um vetor ?????, cujos componentes, :math:`i = 1, 2, \dots, m`, indicam o número de vezes que cada trecho :math:`i` é percorrido no roteiro :math:`j` do avião :math:`v`.

Complete agora o estudo para a programação de operação da frota, admitindo conhecidas as demandas :math:`d_{i}, i = 1, ... , m`, entre cada par de cidades da malha aérea coberta pela empresa.
Comente eventual analogia entre o modelo matemático proposto e modelos de problemas já examinados.


Resolução
---------

.. Se vou da cidade A para B, a demanda é uma, se vou da cidade B para A, a demanda é outra.
.. É um problema dificil, entao comece gerando "problemas viaveis" para cada aeronave. Vamos chamar "roteiro viavel generico j para a aeronave v. Ele vai ter um custo cj e um vetor aij associados."
.. vetor Aij indica quantas vezes o trecho i é coberto pelo roteiro j da aeronave v.
.. É como no problema do corte das bobinas.


Notação
^^^^^^^

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

Função objetivo
^^^^^^^^^^^^^^^

Restrições
^^^^^^^^^^


