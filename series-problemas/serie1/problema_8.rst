8ª QUESTÃO
==========

Uma empresa de navegação, cujos navios porta-contêineres fazem escalas no porto
de Santos, está examinando a construção de um terminal de contêineres vazios no
interior do estado de São Paulo.
Atualmente, a empresa dispõe de um terminal na baixada Santista.

Na importação, os contêineres são transferidos, inicialmente, do porto para os
clientes;
os contêineres vazios retornam ao terminal para inspeção e eventuais reparos
antes de serem reutilizados.
Na exportação, a empresa encaminha os contêineres vazios para os clientes a
partir do mencionado terminal;
os contêineres cheios são encaminhados ao porto.

Para a construção do novo terminal, já há 3 locais pré-selecionados em função de
uma análise preliminar da malha viária e da distribuição espacial dos clientes
da empresa.
Cabe agora aprofundar o estudo, propondo um modelo matemático que ajude a
empresa a decidir se deve construir e onde o novo terminal de contêineres;
mesmo em caso de construção de um novo terminal, o atual pode ser mantido para
atendimento de uma parte dos clientes da empresa.

Especifique as informações necessárias para a tomada de decisões e elabore o
modelo matemático correspondente.


Resolução
---------

O enunciado é bastante aberto e portanto teremos que definir nós mesmos quais seriam os dados relevantes para a tomada de decisão.

Considere as variáveis a seguir:

- :math:`T`: Período de retorno. É o tempo que se estima que o novo terminal de contêineres vazios será utilizado. Por exemplo, se o terminal for utilizado por 10 anos, então :math:`T = 10`. Geralmente essa é um parâmetro importante em projetos de engenharia. Esse tempo começa a contar a partir da inauguração do terminal.
- :math:`j`: índice que representa o local de construção do terminal de contêineres vazios. Com :math:`j = 1, 2, 3`.
- :math:`t`: índice que representa o ano. Com :math:`t = 1, 2, \ldots, T`.
- :math:`C_{j}^{c}`: custo de construção do terminal de contêineres vazios no local :math:`j`.
- :math:`c_{jt}^{op}`: custo de operação anual do terminal de contêineres vazios no local :math:`j` no ano :math:`t`.
- :math:`d_{t}^{imp}`: demanda anual de contêineres vazios para importação no ano :math:`t`.
- :math:`d_{t}^{exp}`: demanda anual de contêineres vazios para exportação no ano :math:`t`.
- :math:`C_{0}^{trans}`: custo de transporte de um contêiner vazio que chega ou sai do terminal antigo.
- :math:`C_{j}^{trans}`: custo de transporte de um contêiner vazio que chega ou sai do terminal novo no local :math:`j`.
- :math:`Q_{t}`: quantidade de contêineres vazios movimentados em um ano :math:`t`.

Variáveis de decisão
^^^^^^^^^^^^^^^^^^^^

- :math:`z_{j}`: variável binária que indica se o terminal de contêineres vazios será construído no local :math:`j` (1) ou não (0). Com :math:`j = 1, 2, 3`.
- :math:`x_{jt}`: variável inteira que indica a quantidade de contêineres movimentados no terminal novo no local :math:`j` no ano :math:`t`.
- :math:`y_{t}`: variável inteira que indica a quantidade de contêineres movimentados no terminal antigo no ano :math:`t`.

Função objetivo
^^^^^^^^^^^^^^^

Queremos minimizar o custo total para a empresa.

#. Custo de construção:

    .. math::

        C^{c} = \sum_{j=1}^{3} C_{j}^{c} \cdot z_{j}

#. Custo de operação:

    O custo de operação do terminal antigo assumiremos fixo e invariantes em relação a construção do novo terminal. \
    Porém o custo de operação do terminal novo depende se ele for construído ou não, do tempo de 

    .. math::

        C^{op} = \sum_{j=1}^{3} \sum_{t=1}^{T} c_{jt}^{op} \cdot z_{j}


#. Custo de transporte

    O custo de transporte é calculado em função da quantidade de contêineres movimentados no terminal antigo e no terminal novo. \
    Podemos assumir que o custo de transporte total em um local será o custo unitário vezes a demanda. 

    .. math::

        C^{transp} = \sum_{t=1}^{T} \left( C_{0}^{trans} \cdot y_{t} + \sum_{j=1}^{3} C_{j}^{trans} \cdot x_{jt} \cdot z_{j} \right)


#. Custo total:
    
    Sendo assim, a função objetivo será: 

    .. math::

        \min \left( C^{c} + C^{op} + C^{transp} \right)


Restrições
^^^^^^^^^^

#. Número de terminais novos:

    Queremos construir no máximo 1 terminal novo. Perceba que podemos construir 0 terminais novos.

    .. math::

        \sum_{j=1}^{3} z_{j} \leq 1

#. Atendimento da demanda:

    A quantidade de contêineres movimentados no terminal antigo e no terminal novo deve ser suficiente para atender a demanda.

    .. math::

        \sum_{t=1}^{T} y_{t} \geq \sum_{t=1}^{T} d_{t}^{imp} + \sum_{t=1}^{T} d_{t}^{exp}

    .. math::

        \sum_{t=1}^{T} \sum_{j=1}^{3} x_{jt} \cdot z_{j} \geq \sum_{t=1}^{T} d_{t}^{imp} + \sum_{t=1}^{T} d_{t}^{exp}


Espaço das variáveis
^^^^^^^^^^^^^^^^^^^^

- :math:`z_{j} \in \{0, 1\}` para todo :math:`j = 1, 2, 3`.
- :math:`x_{jt} \geq 0` para todo :math:`j = 1, 2, 3` e :math:`t = 1, 2, \ldots, T`.
- :math:`y_{t} \geq 0` para todo :math:`t = 1, 2, \ldots, T`.

Comentários
^^^^^^^^^^^

Podemos complicar o modelo tanto quanto quisermos.
Possíveis formas de se complicar o modelo aqui proposto seria:

- Definir capacidades máxima de contêineres que podem ser armazenados no terminal novo (para cada candidato) e antigo.
- Definir custos de transporte entre pares de origem e destino. Ou seja, determinar nós de demanda e associar custos entre eles e os nós que representam os candidatos e o terminal antigo. Isso tornaria o problema bastante parecido com o exercício do Centro de Distribuição (CD) visto em aula.
- Definir custos de transporte variáveis em função da quantidade de contêineres movimentados.


É importante manter um equilíbrio entre a complexidade do modelo e a relevância
das restrições e variáveis consideradas.
Em geral, começa-se com um modelo mais simples e vai-se adicionando complexidade
conforme a necessidade, evitando assim construir um modelo desnecessariamente
complexo.

