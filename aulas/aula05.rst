Aula 05
=======

23 de Julho de 2024.

Programação Linear
------------------

- Na aula passada nós definimos uma forma padrão para o problema de programação linear.
    - Todas as restrições sao na forma de igualdade
    - Trata-se de problemas de minimização.
    - Todas as variáveis sao não negativas.
- Porem, qualquer problema de programação linear pode ser transformado para a forma padrão.
- Na semana passada, também, nós começamos a falar sobre o método Gauss Jordan
- O método Gauss Jordan é uma forma de resolver sistemas lineares e que faz parte do Simplex.
- Professor fez a representação gráfica de um problema e desenhou a região viável.
    - A região viável é o lugar geométrico que contem todos os pontos que satisfazem as
- Professor fala sobre funções equipotenciais.
- Feixe de retas paralelas
- Se altero a função objetivo do problema, eu acabo alterando somente a inclinação da reta.
- A solução geométrica somente pode ser feita se eu conseguir estabelecer 2 ou 3 variáveis isoladas. Mais do que isso, não consigo plotar
- Os vertices da figura sao os pontos que maximizam ou minimizam a função objetivo.
- Para o exemplo em questão, foram binômio(5 2) = 10 possíveis vertices, já que temos 5 variáveis. Porem somente 5 vertices sao de fato pertencentes a região viável.
- Queremos agora construir um método que seja algébrico e não geométrico para encontrar a solução ótima,


Procedimento algébrico para resolver o problema introdutório

1. Escolher duas das 5 variáveis e atribuir valor nulo a essas duas variáveis.
2. Resolver o sistema de equações com 3 variáveis para as outras variáveis
3. verificar se as variáveis sao >= 0. Se todas forem >= 0, passar para o passo 4. Se não, abandonar a solução e voltar para o passo 1.
4. Calcular a função objetivo z (z* = min(z*, z))
5. Voltar ao passo 1

Ou seja, eu não preciso desenhar a região viável. Eu posso simplesmente testar todos os candidatos a vertices e verificar qual deles é o melhor para a função objetivo.

Como voce generalizaria esse procedimento se estou num sistema com N equações e M variáveis?

Apos essa nossa primeira descoberta, chegamos a um numero:
binômio(n n-m) = binômio(n m) alternativas

Ainda assim, vai ser totalmente inviável testar todas as alternativas. Precisamos de um método mais eficiente: Simplex.

Nao vamos querer comparar soluções, o simplex vai me entregar o resultado ótimo do problema.


Busca por um algoritmo eficiente para resolver o Problema de Programação Linear na forma padrão
------------------------------------------------------------------------------------------------

Características desejáveis
~~~~~~~~~~~~~~~~~~~~~~~~~~

1 - saiba reconhecer que uma solução básica viável é ótima ao se deparar com ele (sem necessidade de compara-la com outra solução).
2 - Saiba passar de uma solução básica viável não ótima para uma solução básica viável ótima.

Professor faz aqui um exemplo introdutório
-------------------------------------------

"Forma canônica com relação às variáveis básicas x3, x4 e x5."
x1 e x2 sao chamadas variáveis não básicas.

a função objetivo é função somente das variáveis não básicas

A uma forma canônica, vamos ter associada 1 solução básica. Para tanto, impõe-se valor nulo às variáveis não básicas.
No caso, x2 = x2 = 0 e obtém-se os valores das variáveis básicas.


Se os valores de todas as variáveis básicas sao não negativas, diz-se que a solução básica é viável.

Associação entre geometria e algebra:
- Um vértice esta associado ao uma solução básica
- Um vértice viável esta associado a uma solução básica viável


Professor resolve um exemplo numérico. Mostra que temos que decidir se vamos seguir caminhando pela esquerda ou pela direita.
Em media, olhar somente o primeiro caso já é suficiente para resolver o problema.
Ou seja, a regra muito simples é "começa no 0 e aumenta a variável que tem o coeficiente mais negativo na função objetivo."
Exemplo com z = - 7/8*x1 - 1/2*x2


Constatada que a solução básica na viável inicial (x1=x2=0 portanto x3=4, x4=9/2, x5=2) não é solução ótima de ..., pela analise dos conjuntos de x1 e x2 na função objetivo, manter y2=0 e aumentar x1 (caminhando por um lado da região viável.
Para saber onde interromper a caminhada temos que examinar as especificações do problema (impondo x2 =0).


"Eu olho para uma solução básica viável e pergunto: Ela é ótima?"




