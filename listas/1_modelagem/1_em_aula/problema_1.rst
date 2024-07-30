Questão 1
=========

Enunciado
---------

Considere uma empresa que fabrica um produto cuja demanda é tipicamente sazonal, isto é, ao longo do ano há fortes oscilações na demanda.
Para operar neste mercado, a empresa pode utilizar os seguintes procedimentos:

a. demitir operários no início de um mês;
b. contratar operários no início de um mês;
c. utilizar até 35 horas extras por mês de cada operário, cuja jornada normal mensal totaliza 175 horas;
d. estocar o produto de um mês para o mês seguinte;
e. retardar o atendimento de parte da demanda de um mês para o mês seguinte.

Admita conhecidos:

f. o custo da demissão de um operário (despesa para atender a legislação trabalhista);
g. o custo da contratação de um operário (treinamento);
h. o custo médio do homem-hora extra;
i. o custo de manter uma unidade do produto em estoque de um mês para o mês seguinte;
j. a demanda em cada mês do próximo ano;
k. o número de operários e a quantidade de produto em estoque ao fim deste ano;
l. o salário mensal médio de um operário (sem incluir horas extras);
m. o número de homens-hora para fabricar uma unidade do produto;
n. o desconto concedido por unidade do produto cuja entrega é retardada para o mês seguinte ao da demanda;
o. o número máximo de unidades que podem ser mantidas em estoque de um mês para o mês seguinte;
p. o estoque desejado ao fim do próximo ano.

Proponha um modelo matemático para definir o programa de produção e a política de recursos humanos da empresa para o próximo ano.

Resolução
---------

Simbologia
^^^^^^^^^^

- :math:`C_{dem}`: custo da demissão de um operário. (eq. 'f')
- :math:`C_{con}`: custo da contratação de um operário. (eq. "g")
- :math:`C_{hhr}`: custo médio do homem-hora extra. (eq. "h")
- :math:`C_{arm}`: custo de manter uma unidade do produto em estoque de um mês para o mês seguinte. (eq. "i")
- :math:`D_{t}`: demanda no mês :math:`t`, com :math:`t = 1, 2, \ldots, 12`. (eq. "j")
- :math:`O_{0}`: número de operários ao fim deste ano. (eq. "k")
- :math:`E_{0}`: estoque ao fim deste ano. (eq. "k")
- :math:`S_{ope}`: salário mensal médio de um operário. (eq. "l")
- :math:`H_{hhr}`: número de homens-hora para fabricar uma unidade do produto. (eq. "m")
- :math:`P_{des}`: desconto concedido por unidade do produto cuja entrega é retardada para o mês seguinte ao da demanda. (eq. "n")
- :math:`Q`: capacidade de armazenamento. Número máximo de unidades que podem ser mantidas em estoque de um mês para o mês seguinte. (eq. "o")
- :math:`E_{12}`: Estoque desejado ao fim do próximo ano. (eq. "p")

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

Seja :math:`t` uma variável inteira que representa o mês, com :math:`t = 1, 2, \ldots, 12`.

- :math:`x_{t}` - inteira - Número de funcionários demitidos no início do mês :math:`t`
- :math:`y_{t}` - inteira - Número de funcionários contratados no início do mês :math:`t`
- :math:`z_{t}` - inteira - Número de horas extras utilizadas no mês :math:`t`, somadas as horas extras de todos os funcionários
- :math:`w_{t}` - inteira - Quantidade de produto estocado no mês :math:`t`
- :math:`u_{t}` - inteira - Quantidade de demanda não atendida no mês :math:`i` que será atendida no mês :math:`i+1`, com :math:`i = 1, 2, \ldots, 11`

Variáveis auxiliares
^^^^^^^^^^^^^^^^^^^^

1. Número de operários disponíveis no mês :math:`t`:

    O número de operários disponíveis em um mês :math:`t` é dado pela quantidade \
    de operários ao fim do ano anterior mais a quantidade de operários contratados \
    até antes do mês :math:`t` menos a quantidade de operários demitidos até antes \
    do mês :math:`t`. Ou seja:

    .. math::

        O_{t} = O_{0} + \sum_{j=1}^{t} y_{j} - \sum_{k=1}^{t} x_{k}, \quad \forall t \in \{ 1, 2, \ldots, 12 \} \subset \mathbb{Z}

2. Número de horas disponíveis no mês :math:`t`:

    Tendo posse do número total de funcionários disponíveis, é possível calcular o \
    número total de horas disponíveis no mês :math:`t`, para isso multiplicamos a \
    quantidade de operários disponíveis no mês :math:`t` pela jornada normal mensal \
    de cada operário, que é de 175 horas. Soma-se a isso o número de horas extras \
    utilizadas no mês :math:`t`:

    .. math::
        H_{t} = 175 \cdot O_{t} + z_{t}, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

3. Quantidade de produto produzido no mês :math:`t`:

    A produção de um mês é facilmente calculada dividindo-se o número de horas \
    disponíveis no mês :math:`t` pelo número de homens-hora para fabricar uma unidade \
    do produto:

    .. math::
        q_{t} \leq \frac{H_{t}}{H_{hhr}}, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

4. Demanda atendida no mês :math:`t`:

    A demanda atendida no mês :math:`t` é a demanda total do mês menos a quantidade \
    de demanda não atendida no mês :math:`t` (que será postergada para o mês seguinte):

    .. math::
        d_{t} = D_{t} - u_{t}, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

5. Quantidade de produto estocado no mês :math:`t`:

    Já para a quantidade de estoque, devemos tomar em conta que o estoque do mês \
    anterior mais a produção do mês menos a demanda atendida do mês é igual ao \
    estoque do mês atual:

    .. math::
        E_{t} = E_{0} + \sum_{j=1}^{t} (q_{j} - d_{j} - w_{j}), \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}


Função objetivo
^^^^^^^^^^^^^^^

Minimizar o custo total da empresa, que é a soma dos custos de demissão, contratação, horas extras, armazenamento e penalidades de atraso.

#. Custo de demissão:
    .. math::
        f_{dem} := \sum_{t=1}^{12} C_{d} \cdot x_{t}


#. Custo de contratação:
    .. math::
        f_{con} := \sum_{t=1}^{12} C_{c} \cdot y_{t}

#. Custo relativo ao salario dos funcionários:
    .. math::
        f_{sal} := \sum_{t=1}^{12} S_{ope} \cdot O_{t}

#. Custo de horas extras:
    .. math::
        f_{hor} := \sum_{t=1}^{12} C_{h} \cdot z_{t}

#. Custo de armazenamento:
    .. math::
        f_{arm} := \sum_{t=1}^{12} C_{arm} \cdot w_{t}

#. Penalidades de atraso da demanda:
    .. math::
        f_{pen} := \sum_{t=1}^{11} P_{d} \cdot u_{t}

A função, portanto, deverá ficar com a seguinte forma:

.. math::

    \min \left( f_{dem} + f_{con} + f_{sal} + f_{hor} + f_{arm} + f_{pen} \right) =

    \min \left( \sum_{t=1}^{12} C_{d} \cdot x_{t} + \sum_{t=1}^{12} C_{c} \cdot y_{t} +  \sum_{t=1}^{12} S_{ope} \cdot O_{t} + \sum_{t=1}^{12} C_{h} \cdot z_{t} + \sum_{t=1}^{12} C_{arm} \cdot w_{t} + \sum_{t=1}^{11} P_{d} \cdot u_{t} \right)

Restrições
^^^^^^^^^^

.. Professor recomendou olhar restrições de demanda mês a mês, e não a demanda total do ano. Isso pq vc pode acabar não dando conta de atender a demanda total. 
.. Ele sugere algo como: p_{j} + e_{j-1} + da_{j} = d_{j} + e_{j} + 

#. Restrição de demanda (eq. "j" e "m")

    Ao final do último mês, todas as demandas devem ser necessariamente atendidas:

    .. math::

        \sum_{t=1}^{12} d_{t} = \sum_{t=1}^{12} D_{t}


#. Restrição de horas extras.

    Sabemos que o número de horas extras máximas de cada funcionário é de 35 horas. Portanto:

    .. math::

        z_{t} \leq 35 \cdot O_{t}, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}


#. Restrição de capacidade de armazenamento (eq. "o")

    Sabemos que o estoque no mes :math:`t` nunca pode ser superior à capacidade máxima do armazém (:math:`Q`).

    .. math::

        w_{t} \leq Q, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}


#. Estoque desejado ao fim do próximo ano (eq. "p")

    O estoque do último mês já está definido, portanto:

    .. math::

        w_{12} = E_{12}


#. Espaço das variáveis.

    Restrições de não negatividade (estoque, horas extras, contratação, demissão, demanda não atendida)

    .. não é somente dizer que a variável é não negativa, mas sim especificar o espaço de busca (dizer que sao inteiras importa).

    Apesar de parecer óbvias em muitos dos casos, podemos definir explicitamente:

    .. math::

        w_{t} \geq 0, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

        z_{t} \geq 0, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

        y_{t} \geq 0, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

        x_{t} \geq 0, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

        u_{t} \geq 0, \quad \forall t \in \{1, 2, \ldots, 11 \} \subset \mathbb{Z}

        E_{t} \geq 0, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

        O_{t} \geq 0, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

        H_{t} \geq 0, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

        d_{t} \geq 0, \quad \forall t \in \{1, 2, \ldots, 12 \} \subset \mathbb{Z}

