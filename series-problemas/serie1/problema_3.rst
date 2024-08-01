3ª QUESTÃO
==========

Uma empresa de transporte aéreo dispõe de uma frota de :math:`N_{v}` aeronaves;
a aeronave :math:`v`, :math:`v = 1, 2, \dots, N_{v}`, dispõe de :math:`K_{v}`
poltronas para o transporte de passageiros.
A empresa oferece um serviço sem escalas e opera voos entre :math:`m` pares de
cidades (o voo entre a cidade A e a cidade B, para efeito dessa contagem, é
distinto do voo entre a cidade B e a cidade A)

A empresa utiliza uma única cidade-base para sua frota e os primeiros voos do
dia de cada aeronave começam e os últimos voos do dia terminam nessa cidade;
fora essas restrições, cada aeronave pode, ao longo do dia, ser utilizada em
diversos trechos da malha aérea coberta pela empresa.

Numa etapa inicial, para programar a operação da frota, foi desenvolvido um
estudo que determinou, para cada avião da frota, os diversos roteiros diários
viáveis, começando e terminando na cidade-base.
Cada roteiro viável :math:`j` de uma aeronave :math:`v` é identificado por um
parâmetro :math:`c_{vj}`, que representa o seu custo operacional e um vetor
:math:`A_{vij}`, cujos componentes, :math:`i = 1, 2, \dots, m`, indicam o número
de vezes que cada trecho :math:`i` é percorrido no roteiro :math:`j` do avião
:math:`v`.

Complete agora o estudo para a programação de operação da frota, admitindo
conhecidas as demandas :math:`d_{i}, i = 1, ... , m`, entre cada par de cidades
da malha aérea coberta pela empresa.

Comente eventual analogia entre o modelo matemático proposto e modelos de
problemas já examinados.


Resolução
---------

Existe uma parte interessante desse problema que é o aproveitamento dos voos.
Aproveitamento é definido, em engenharia de transporte aéreo, como o número de
assentos ocupados divido pelo número de assentos disponíveis.
No nosso caso vamos ignorar o aproveitamento dos voos e assumir que o mais
importante é que tenhamos assentos (ou poltronas) suficientes para atender a
demanda entre cada par de cidades.

Notação
^^^^^^^

- :math:`v` é o índice da aeronave, com :math:`v = 1, 2, \ldots, N_{v}`.
- :math:`K_{v}` é o número de poltronas disponíveis na aeronave :math:`v`.
- :math:`m` é o número de pares de cidades, com :math:`m = 1, 2, \ldots, m`.
- :math:`d_{i}` é a demanda entre o par de cidades :math:`i`, com :math:`i = 1, 2, \ldots, m`.
- :math:`c_{vj}` é o custo operacional do roteiro :math:`j` da aeronave :math:`v`.
- :math:`A_{vij}` é o número de vezes que o trecho :math:`i` é percorrido no roteiro :math:`j` da aeronave :math:`v`.

Perceba que o índice :math:`j` representa todos os roteiros viáveis para a
aeronave :math:`v` e o índice :math:`i` representa todos os pares de cidades.

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

Seja :math:`x_{vj}` é uma variável binária que indica se o roteiro :math:`j` da
aeronave :math:`v` é escolhido ou não.


Função objetivo
^^^^^^^^^^^^^^^

Queremos minimizar o custo total de operação da frota, que neste caso será
representado pelo somatório de custos operacionais de cada roteiro selecionado.
Existe uma série de custos fixos associados a cada aeronave que será ignorada
por simplicidade e porque o enunciado não fornece informações suficientes para
modelar esses custos.
Sendo assim, a função objetivo é:

.. math::

   \min \sum_{v=1}^{N_{v}} \sum_{j} c_{vj} \cdot x_{vj}, \quad \forall v \in \{1, \ldots, N_{v}\} \quad \forall j

O índice :math:`j` representa todos os roteiros viáveis para a aeronave :math:`v`.
Não é fornecido no enunciado o número de roteiros viáveis para cada aeronave,
então vamos deixar o somatório sobre :math:`j` sem limites, assim subentende-se
que estamos somando para todos os roteiros :math:`j`.

Restrições
^^^^^^^^^^

#. Atendimento da demanda

    O mais óbvio do problema é que precisamos atender a demanda. \
    Aqui existe uma sutileza que é o fato de que o exercício não fala qual a \
    unidade de medida da demanda, poderia ser passageiros ou número de voos. \
    Conhecendo o problema, é mais intuitivo pensar que a demanda é o número de \
    passageiros que precisa ser transportado entre o par de cidades. \

    Sendo assim, queremos que o número de voos vezes o numero de poltronas \
    disponíveis seja maior ou igual a demanda entre cada par de cidades.

    .. math::

        \sum_{v=1}^{N_{v}} \sum_{j} A_{vij} \cdot x_{vj} \cdot K_{v} \geq d_{i}, \quad \forall i \in \{1, \ldots, m\}

#. Capacidade

    É verdade que o enunciado não fala nada sobre capacidade ou limite de roteiros \
    que uma aeronave pode fazer, mas é razoável pensar que uma aeronave não pode \
    fazer mais de um roteiro por dia.

    .. math::

        \sum_{j} x_{vj} \leq 1, \quad \forall v \in \{1, \ldots, N_{v}\}


Espaço das variáveis
^^^^^^^^^^^^^^^^^^^^

.. math::

   x_{vj} \in \{0, 1\}, \quad \forall v \in \{1, \ldots, N_{v}\} \quad \forall j


Comentários
-----------

O um problema complexo que foi bastante simplificado pelo fato de que os
possíveis roteiros para cada aeronave já foram determinados previamente.
caso não tivessem sido determinados, o problema seria análogo a um problema de
roteirização de veículos.

Este exercício é parecido com o exercício 6 visto em classe,
pois trata-se de um problema de designação.
Para cada aeronave, vou designar um dos :math:`j` possíveis roteiros.
De certa forma, também é bastante parecido com o exercício 7 de corte das bobinas,
somente com a mudança de que dessa vez a matrix :math:`A_{vij}` já foi determinada
pelo enunciado.

