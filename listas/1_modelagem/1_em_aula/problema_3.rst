Questão 3
=========

Enunciado
---------

Uma pequena oficina de usinagem fabrica um conjunto formado por 4 peças diferentes
e dispõe de 6 máquinas diferentes para executar tal serviço.
A máquina :math:`i` pode fabricar :math:`n_{ij}` peças do tipo :math:`j` por dia,
se alocada exclusivamente à produção desta peça.

a.  Admitindo que seja desprezível o tempo de ajuste de qualquer máquina, quando \
    passa da usinagem de um tipo de peça para outro, formule um modelo matemático \
    para alocar o tempo de cada máquina à produção das diferentes peças.  

b.	Admitindo, porém, que o tempo de ajuste de qualquer máquina para passar da \
    peça 3 para qualquer tipo de peça (e reciprocamente) fosse muito grande, como \
    deveria ser distribuído o tempo de cada máquina para maximizar o número de \
    conjuntos produzidos num único dia. 

Resolução
---------

Sabemos que :math:`i = 1, 2, 3, 4, 5, 6` (máquinas) e :math:`j = 1, 2, 3, 4` (peças).

Seja :math:`x_{ij}` a quantidade de peças do tipo :math:`j` produzidas pela máquina :math:`i`,
com :math:`x_{ij} \geq 0, \quad \forall i,j`. um subconjunto dos números inteiros.

a.  Modelo matemático para alocar o tempo de cada máquina à produção das diferentes peças:

    Definimos uma variável :math:`\alpha_{ij}` que indica a fração do tempo da máquina :math:`i` dedicada a produção da peça :math:`j`.
    Quantidade de conjuntos montados (y):

    .. math::

        y = min(x_{j}) \quad \forall j = 1, 2, 3, 4

        y = min \left( \sum_{i=1}^{6} \alpha_{ij} \cdot n_{ij} \right) \quad \forall j = 1, 2, 3, 4

    .. math::

        max(y)

    subject to:

    .. math::

        \sum_{j=1}^{4} \alpha_{ij} \leq 1, \quad \forall i = 1, 2, 3, 4, 5, 6

    
    Convenientemente, podemos linearizar a definição de y, que é uma restrição logica, substituindo por restrições algébricas.
    Vamos à linearização:

    .. math::

        y \leq x_{j} \quad \forall j = 1, 2, 3, 4

    Note que: :math:`\alpha_{ij}` deve ser maior igual a 0. :math:`x_{ij}` maior igual a zero inteiro e y maior igual a zero inteiro.
        

b. Modelo com consideração de setup time:

    Aqui podemos fazer algumas hipóteses. Como o enunciado diz que o tempo de setup é muito grande
    para passar da peça 3 para qualquer outra, podemos considerar que jamais haverá setup de ou 
    para a peça 3. Assim, algumas máquinas podem ser alocadas exclusivamente para a produção da
    peça 3, enquanto outras podem ser alocadas para a produção das peças 1, 2 e 4.


    .. math::

        x_3 = \sum_{i=1}^{6} z_i \cdot n_{i3}

    Se :math:`z_{4} = 1`, a máquina 4 somente usina a peça 3.
    Então quanto vale :math:`\alpha_{41}`, :math:`\alpha_{42}` e :math:`\alpha_{43}`?

    .. math::

        z_{4} + \sum_{j=1 \neq 3}^{4} \alpha_{4j} = 1

    Podemos generalizar a última equação para todas as máquinas:

    .. math::

        z_{i} + \alpha_{i1} + \alpha_{i2} + \alpha_{iy} \leq 1

