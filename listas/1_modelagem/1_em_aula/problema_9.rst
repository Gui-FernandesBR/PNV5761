Problema 9
==========

Problema tipico de atendimento de emergências, onde a prioridade não é custo, senão que o atendimento à população.

Enunciado
---------

Parte A
^^^^^^^

Em uma cidade, subdividida em :math:`m` regiões, há :math:`n` locais candidatos ao recebimento de um posto de corpo de bombeiros.
Deseja-se minimizar o custo de instalação garantindo-se, porém, que cada região possa ser atendida por uma viatura dentro de um tempo limite especificado, :math:`T`.
Propor um modelo matemático para definir os locais de instalação de postos de corpo de bombeiros.

Sugestão: Admitir que, para qualquer região :math:`j` da cidade, são conhecidos os locais candidatos à instalação do posto que satisfazem a restrição de tempo do atendimento.
Isto é, admitir que seja conhecida uma matriz :math:`A = [aij]`, i=1,2,...,n; j=1,2,..., m tal que:
:math:`a_{ij} = 1` se :math:`t_{ij} <= T` e 0 caso contrário.

Parte B
^^^^^^^

.. Questão não socialmente aceita.

No caso de haver restrição orçamentária que não permita o atendimento de todas as regiões e conhecendo a população :math:`p_{j}` de cada região :math:`j`, proponha o modelo para instalação de :math:`q` postos de corpo de bombeiros.


Parte C 
^^^^^^^

Se uma região pode ser atendida, dentro do limite de tempo especificado, por um único posto, pode ocorrer que, em caso de acidente na região considerada, se os veículos do posto estão atendendo outra emergência, não haja como controlar o acidente.
Por isto, uma outra estratégia de alocação e priorizar a instalação de postos que propiciem cobertura reserva para cada região.

No caso de haver restrição orçamentária que não permita uma cobertura reserva para todas as regiões (embora se possa garantir o atendimento simples de qualquer região) e conhecendo a população :math:`p_{j}` de cada região :math:`j`,  proponha  o  modelo  para  a  instalação de :math:`r` postos (r < n).

Resolução
---------

Parte A
^^^^^^^

Considere a variável binária :math:`x_{i}` que indica se o local :math:`i` foi escolhido para instalação do posto de bombeiros.

.. xi = 1 se for instalado um posto de bombeiros no local i, 0 caso contrario.

Função Objetivo
""""""""""""""""

Vamos minimizar o numero de postos instalados, já que o enunciado não fala de custos ou coisas do tipo.

.. math::

    \sum_{i=1}^{m} x_{i}

Restrições
""""""""""

Bom, queremos garantir que ao menos um posto atenda cada região.
Isso só é possível caso saibamos de antemão que existe pelo menos 1 local que atende a região j, para toda região j.
Então: 

.. math::

    \sum_{i=1}^{m} a_{ij} \cdot x_{i} \geq 1, \forall j = 1, 2, ..., m

Espaço das variáveis
""""""""""""""""""""

xi = 0 ou 1

Parte B
^^^^^^^

Teremos a seguinte restrição: 

.. math::

    \sum_{i=1}^{n} x_{ij} \leq q, \forall j = 1, 2, ..., m

Porém note que essa inequação não garante que todas as regiões serão atendidas. 
Então definimos a "restrição asterisco" abaixo:

.. math::

    \sum_{i=1}^{m} a_{ij} \cdot x_{i} \geq 1, \forall j = 1, 2, ..., m


Função objetivo
""""""""""""""""

Queremos maximizar a população coberta.

Queremos maximizar a somatório: :math:`\sum_{j=1}^{m} p_{j} \cdot y_{j}`

:math:`y_{j} = 1` se a região j é coberta (restrição asterisco é atediada), 0 caso contrario.

Como escrever algebricamente que :math:`y_{1} = 1` somente se a restrição asterisco é satisfatório?

.. math::

    \sum_{i=1}^{n} a_{ij} \cdot x_{i} \geq y_{j}
    
    or

    y_{j} \leq \sum_{i=1}^{n} a_{ij} \cdot x_{i}

Ou seja, queremos maximizar :math:`P_{c}` tal que:

.. math::

    P_{c} = \sum_{j=1}^{m} p_{j} \cdot y_{j}

sujeito às seguintes restrições:

.. math::
    
    y_{i} \leq \sum_{i=1}^{n} a_{ij} \cdot x_{i}, \forall j \in {1, 2, ..., n}

    q \geq \sum_{i=1}^{n} x_{i}

Espaço das variáveis: xi = 0 ou 1; yi = 0 ou 1

Parte C
^^^^^^^

Quero maximizar a população da cidade que tenha cobertura reserva.
Diz-se que uma região :math:`j` tem cobertura reserva se ela pode ser atendida, em intervalo de tempo :math:`T`, por pelo menos 2 postos de bombeiro.

.. math::

    \sum_{i=1}^{n} a_{ij} \cdot x_{i} \geq 2,

Introduzimos, então, uma nova variável binária :math:`w_{j}` que indica se a região :math:`j` tem cobertura reserva (restrição acima atendida) ou não.

Agora podemos formalizar matematicamente:

Função objetivo:
""""""""""""""""

Seja :math:`P_{cr}` a população coberta com cobertura reserva.
Queremos maximizar :math:`P_{cr}` tal que:

.. math::
    P_{cr} = \sum_{j=1}^{m} p_{j} \cdot w_{j}

Restrições
""""""""""

Sujeito às seguintes restrições:

.. math::
    
    w_{i} \leq \sum_{i=1}^{n} a_{ij} \cdot x_{i} - 1, \quad \forall j \in {1, 2, ..., n}

Porém quero garantir que todas as regiões tenham ao menos uma cobertura simples.
Poderíamos colocar essa restrição, porem ela seria redundante. Ainda assim, escrevemos:

.. math::
    
    \sum_{i=1}^{n} a_{ij} \cdot x_{i} \geq 1, \forall j \in {1, 2, ..., n}


.. O "-1" aqui é interessantíssimo.


Espaço das variáveis: :math:`x_{i}` = 0 ou 1; :math:`y_{i}` = 0 ou 1; :math:`w_{j}` = 0 ou 1




