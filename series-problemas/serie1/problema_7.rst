7ª QUESTÃO
==========

Conforme visto em aula, a principal preocupação com o modelo matemático do problema do caixeiro viajante é a seleção do conjunto de restrições para impedir a formação de roteiros que não contenham todas as cidades (formação de sub-roteiros).
Uma formulação diferente para evitar a formação de sub-roteiros introduz variáveis :math:`y_{ij}`, para representar o fluxo entre os nós :math:`i` e :math:`j`, e admite que há uma oferta de :math:`(n-1)` unidades de um produto na cidade base (nó 1) e que cada uma das outras :math:`(n-1)` cidades tenha uma demanda igual a 1.
As restrições para evitar a formação de sub-roteiros são:

..  math::

    \sum_{j=2}^{n} y_{1j} = n-1

    \sum_{j=1, j \neq i}^{n} y_{ij} - \sum_{k=1, k \neq i}^{n} y_{ki} = - 1, \quad \forall i \in \{2, 3, \dots, n\}

    y_{ij} \leq M \cdot x_{ij}, \quad \forall i,j \in \{1, 2, \dots, n\}, i \neq j


em que :math:`M` é qualquer real maior ou igual a :math:`n-1`.

Interprete como essas restrições evitam a formação de sub-roteiros.


Resolução
---------

Essa é a abordagem de problema de transbordo para o problema do caixeiro viajante.

#. Restrição de oferta na cidade base:

    .. math::

        \sum_{j=2}^{n} y_{1j} = n-1

    Essa restrição garante que a cidade base (nó 1) envia exatamente \
    :math:`n-1` unidades para as outras cidades, o que significa que todas as \
    outras cidades (2 a n) devem receber exatamente uma unidade cada uma. Isso \
    assegura que o fluxo total que sai da cidade base corresponde ao número de cidades a serem visitadas, garantindo a inclusão de todas as cidades no \
    roteiro.

#. Restrição de fluxo para cada cidade:

    .. math::

        \sum_{j=1, j \neq i}^{n} y_{ij} - \sum_{k=1, k \neq i}^{n} y_{ki} = - 1, \quad \forall i \in {2, 3, \dots, n}

    Essas restrições garantem que cada cidade diferente da cidade base (cidades \
    2 a n) recebe duas unidades e envia exatamente uma unidade. Isso \
    força o modelo de modo que cada cidade deve ter um saldo de uma unidade \
    após receber e enviar unidades, mantendo o ciclo único que passa por \
    todas as cidades. Isso evita sub-roteiros pois cada cidade passa a estar \
    de certa forma "conectada" a cidade base. Contudo, ainda é necessário \
    manter a restrição de que cada nó só pode ser visitado uma vez.

#. Restrição de vínculo entre fluxo e rota:

    .. math::

        y_{ij} \leq M \cdot x_{ij}, \quad \forall i,j \in {1, 2, \dots, n}, i \neq j

    Essa restrição vincula as variáveis de fluxo :math:`y_{ij}` às variáveis de \
    decisão :math:`x_{ij}` (que determinam se uma rota entre as cidades :math:`i` \
    e :math:`j` é usada). O valor :math:`M` assegura que o fluxo entre duas \
    cidades só pode existir se a rota correspondente estiver incluída no \
    roteiro do caixeiro viajante.


Comparação
^^^^^^^^^^

Essa abordagem é uma forma mais eficiente de se garantir que não hajam 
sub-ciclos, pois haverá menos alternativas de solução.
Vamos compará-la com o modelo Danzig-Fulkerson-Johnson que vimos em aula.

Com auxílio do software CPLEX, vamos resolver o problema do caixeiro viajante
para um conjunto de cidades aleatórias e comparar as soluções obtidas com
os dois modelos.

.. image:: series-problemas/serie1/output1.png
    :align: center
    :width: 500px

.. image:: series-problemas/serie1/output2.png
    :align: center
    :width: 500px

Para um teste de até 100 nós (cidades) clientes, podemos ver pelas imagens que o método estudado nesta questão, baseado no problema do transbordo, é mais computacionalmente eficiente do que o método visto anteriormente.
Enquanto o tempo de execução do método tradicional de Danzig cresce exponencialmente, o método de transbordo cresce de forma mais controlada.
