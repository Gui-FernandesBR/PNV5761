Aula 10
=======

Já terminamos o segundo módulo da disciplina, agora vamos para o último tópico,
que será problemas de fluxo em redes (problemas de transbordo).

O Problema do Transbordo
-------------------------

- Cada nó tem:
    - um conjunto de arcos entrando
    - um conjunto de arcos saindo.
    - um parâmetro indicando oferta (positivo) ou demanda (negativo).
- Cada arco tem um custo unitário associado.
- No exemplo inicial, há um equilíbrio entre oferta e demanda
- O problema consiste em: como atender todas aas demandas gastando o mínimo possível?
- As variáveis de decisão são o fluxo em cada arco.
- Função objetivo: minimizar o custo total. Multiplicar o custo unitário pelo fluxo em cada arco.
- Convenção: escrever primeiro o arco que sai, depois o que entra: :math:`x_{ij}` é o fluxo de :math:`i` para :math:`j`.
- Como restrições, temos:
    - Balanço de massa: a soma dos fluxos que entram em um nó é igual à soma dos fluxos que saem.
    - Não negatividade: :math:`x_{ij} \geq 0`.
- a natureza das restrições: x_ij - A_ij, onde A_ij sempre terá uma componente positiva e outra negativa para cada coluna.
- Essas são restrições muito bem estruturada.
- O simplex revisado funciona bem para matrizes pouco densas.
- A ideia vai ser particularizar o simplex revisado para o problema do transbordo.
- Não precisamos de todas as equações, sempre uma delas é redundante. Professor não quer perder tempo provando este ponto.
- Vamos manter todas as restrições (i.e. todos os pis), mesmo que haja redundância em uma das restrições.
- Fazer Gauss Jordan dá trabalho... Podemos fazer de modo mais rápido ainda.
- Vamos verificar a otimalidade da solução.
- Precisamos formalizar o algoritmo.
- O problema todo é encontrar uma solução básica inicial para o problema, o que não é nada trivial.



