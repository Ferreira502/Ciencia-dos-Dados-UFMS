# Atividade 04 - Pensamento Computacional

## Titulo da proposta
EcoColeta: jogo educativo em Scratch para incentivar o descarte correto de residuos reciclaveis

## 1. Descricao do problema
Um problema comum no cotidiano de escolas, bairros e espacos publicos e o descarte incorreto de residuos reciclaveis. Muitas pessoas querem colaborar com a coleta seletiva, mas ainda possuem duvidas sobre onde descartar papel, plastico, vidro e metal. Esse erro dificulta a reciclagem, aumenta o volume de lixo comum e reduz o reaproveitamento de materiais.

Na comunidade escolar, esse problema aparece principalmente em momentos de lanche, eventos e uso compartilhado de salas. Garrafas plasticas, latas e papeis sao jogados no lixo errado por falta de orientacao imediata e de uma forma simples de aprendizado.

Os principais desafios do problema sao:
- falta de conhecimento sobre a separacao correta dos residuos;
- pouca estimulacao para aprender o tema de forma pratica;
- dificuldade de transformar orientacoes teoricas em uma acao rapida no dia a dia.

## 2. Solucao digital proposta
A solucao proposta e um jogo educativo desenvolvido no Scratch chamado **EcoColeta**. Nele, o jogador deve arrastar um residuo ate a lixeira correta. Cada acerto gera pontos e uma mensagem positiva. Cada erro gera uma orientacao curta explicando a separacao correta. Ao final, o jogador visualiza sua pontuacao e recebe incentivo para aplicar o aprendizado no cotidiano.

Essa solucao foi escolhida porque o Scratch permite criar prototipos interativos com facilidade, usando blocos visuais, personagens, cenarios, pontuacao, tempo e mensagens educativas.

## 3. Aplicacao dos pilares do Pensamento Computacional

### 3.1 Decomposicao
O problema foi dividido em partes menores para facilitar o planejamento da solucao:
- identificar os tipos principais de residuos reciclaveis;
- definir as lixeiras correspondentes;
- criar a mecanica de interacao do jogador;
- registrar acertos, erros e pontuacao;
- exibir mensagens educativas e tela final.

### 3.2 Reconhecimento de padroes
Foram observados padroes no problema:
- os mesmos tipos de residuos aparecem com frequencia no dia a dia;
- os erros de descarte costumam se repetir;
- a aprendizagem melhora quando a pessoa recebe retorno imediato sobre acerto ou erro.

Esses padroes ajudaram a definir um jogo com repeticao controlada, feedback instantaneo e categorias simples de materiais.

### 3.3 Abstracao
Para tornar o problema viavel em uma ferramenta educacional, foi feita uma simplificacao:
- foram considerados apenas quatro grupos principais: papel, plastico, vidro e metal;
- cada rodada apresenta um unico residuo por vez;
- o foco do jogo nao e modelar todo o sistema de coleta da cidade, mas ensinar a decisao correta de separacao.

Assim, a solucao destaca somente os elementos essenciais para o aprendizado.

### 3.4 Desenvolvimento de algoritmos
O funcionamento do jogo segue uma sequencia logica:
1. iniciar o jogo e zerar a pontuacao;
2. definir um tempo de partida;
3. sortear um residuo;
4. mostrar o residuo ao jogador;
5. verificar em qual lixeira o jogador tentou descartar;
6. comparar a lixeira escolhida com o tipo correto do residuo;
7. atualizar pontuacao e mensagem de retorno;
8. repetir ate o tempo acabar;
9. exibir resultado final.

## 4. Representacao da solucao no Scratch
No Scratch, a aplicacao pode ser organizada da seguinte forma:

### Cenario
- plano de fundo com o titulo "EcoColeta";
- contador de tempo;
- variavel de pontuacao;
- instrucao curta: "Arraste o lixo ate a lixeira certa e clique na lixeira".

### Atores
- 1 ator para o residuo atual, com varias fantasias;
- 4 atores para as lixeiras: papel, plastico, vidro e metal;
- 1 ator opcional para mensagens ou narrador.

### Interacao
- o residuo aparece no centro superior da tela;
- o jogador arrasta o residuo;
- ao posicionar sobre uma lixeira e clicar nela, o jogo valida a resposta;
- o jogo mostra "Acertou!" ou "Tente novamente!" e carrega o proximo item.

## 5. Resultado esperado
Espera-se que o jogo contribua para a conscientizacao sobre coleta seletiva, reforcando o aprendizado de forma ludica, rapida e acessivel. A proposta pode ser usada em sala de aula, feiras escolares ou atividades de extensao com a comunidade.

## 6. Observacao sobre a implementacao
Junto desta proposta, foi preparado um roteiro de blocos para montagem do jogo no Scratch no arquivo `scratch_blocos.md`.
