Aula 09
=======

- Data: 20 de agosto de 2024.

Análise de Sensibilidade
------------------------

Na aula da semana passada nós começamos a estudar o último tópico: análise de Sensibilidade.

Vamos fazer modificações no modelo matemático da forma padrão.

Precisamos saber quais são as relações entre os coeficientes da forma canônica (coeficientes da tabela simplex) e os coeficientes da forma padrão.

A gente modifica os coeficientes da tabela anteriormente ótima. Problemas?
1. Perder otimalidade (surgir um \bar{c}_{j} < 0).
2. Perder viabilidade (surgir um \bar{b}_{i} < 0).

Se a gente perde otimalidade, a gente precisa fazer um novo passo simplex a partir da tabela alterada.
Agora, se surgir um \bar{b}_{i} < 0, a gente precisa de um novo algoritmo (dual simplex).
O simplex não dá conta de resolver problema fora da região viável.
Apesar de que o método das duas fases também resolve problemas fora da região viável, ele é muito mais lento.

Essa é, basicamente, a nossa forma de fazer análise de sensibilidade.

As equações 8 e 9 do pdf continuação 3 são essenciais para realizar a análise de sensibilidade.

O vetor pi (multiplicadores simplex) é peça fundamental do algoritmo simplex revisado.

Falamos sobre o problema exemplo dessa lista.

A tabela do simplex revisado tem que ter sempre p-1 e o vetor pi.

Teve uma hora ali por volta da pagina 93 +/- em que a encerra o paragrafo com "15", mas o prof disse para considerar como "19"

.. avisos:
.. - a terceira lista vai ser sobre analise de sensibilidade.
.. - haverá uma prova a serie 2 e uma prova para a serie 3
.. - professor vai incluir no dia 10 no calendário pois tivemos um feriado.
.. lista 5 deve ser algo mais simples, algo menor.

O algoritmo dual simplex
------------------------

.. pagina 118

