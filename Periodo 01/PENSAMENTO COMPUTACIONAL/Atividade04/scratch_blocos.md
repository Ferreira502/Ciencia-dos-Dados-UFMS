# Roteiro dos blocos do Scratch - EcoColeta

## Variaveis
- `pontuacao`
- `tempo`
- `itemAtual`
- `tipoAtual`

## Atores
- `Lixo`
- `Lixeira Papel`
- `Lixeira Plastico`
- `Lixeira Vidro`
- `Lixeira Metal`

## Fantasias do ator `Lixo`
- jornal
- caderno
- garrafa plastica
- copo plastico
- garrafa vidro
- pote vidro
- lata
- tampa metal

## Plano de montagem
1. Crie um cenario com o titulo `EcoColeta`.
2. Posicione as quatro lixeiras na parte de baixo da tela.
3. Deixe o ator `Lixo` nascer no topo ou no centro.
4. Ative o modo arrastavel no ator `Lixo`.
5. Crie as variaveis listadas acima para todos os atores.

## Codigo do palco
```text
quando bandeira verde for clicada
defina [pontuacao v] para (0)
defina [tempo v] para (60)
mostre variavel [pontuacao v]
mostre variavel [tempo v]
transmita [novo item v]
repita ate <(tempo) = [0]>
  espere (1) segundos
  mude [tempo v] por (-1)
fim
transmita [fim de jogo v]
```

## Codigo do ator `Lixo`
```text
quando bandeira verde for clicada
va para x: (0) y: (120)
defina modo de arrastar [arrastavel v]
esconda

quando eu receber [novo item v]
mostre
va para x: (0) y: (120)
defina [itemAtual v] para (numero aleatorio entre (1) e (8))

se <(itemAtual) = (1)> entao
  mude para a fantasia [jornal v]
  defina [tipoAtual v] para [papel]
fim

se <(itemAtual) = (2)> entao
  mude para a fantasia [caderno v]
  defina [tipoAtual v] para [papel]
fim

se <(itemAtual) = (3)> entao
  mude para a fantasia [garrafa plastica v]
  defina [tipoAtual v] para [plastico]
fim

se <(itemAtual) = (4)> entao
  mude para a fantasia [copo plastico v]
  defina [tipoAtual v] para [plastico]
fim

se <(itemAtual) = (5)> entao
  mude para a fantasia [garrafa vidro v]
  defina [tipoAtual v] para [vidro]
fim

se <(itemAtual) = (6)> entao
  mude para a fantasia [pote vidro v]
  defina [tipoAtual v] para [vidro]
fim

se <(itemAtual) = (7)> entao
  mude para a fantasia [lata v]
  defina [tipoAtual v] para [metal]
fim

se <(itemAtual) = (8)> entao
  mude para a fantasia [tampa metal v]
  defina [tipoAtual v] para [metal]
fim

quando eu receber [acertou v]
esconda
espere (0.3) segundos
transmita [novo item v]

quando eu receber [fim de jogo v]
esconda
```

## Codigo da `Lixeira Papel`
```text
quando este ator for clicado
se <<tocando em [Lixo v] ?> e <(tipoAtual) = [papel]>> entao
  mude [pontuacao v] por (1)
  diga [Acertou! Papel reciclavel.] por (1) segundos
  transmita [acertou v]
senao
  se <tocando em [Lixo v] ?> entao
    diga [Esse item nao vai no papel.] por (1) segundos
  fim
fim
```

## Codigo da `Lixeira Plastico`
```text
quando este ator for clicado
se <<tocando em [Lixo v] ?> e <(tipoAtual) = [plastico]>> entao
  mude [pontuacao v] por (1)
  diga [Acertou! Plastico separado corretamente.] por (1) segundos
  transmita [acertou v]
senao
  se <tocando em [Lixo v] ?> entao
    diga [Esse item nao vai no plastico.] por (1) segundos
  fim
fim
```

## Codigo da `Lixeira Vidro`
```text
quando este ator for clicado
se <<tocando em [Lixo v] ?> e <(tipoAtual) = [vidro]>> entao
  mude [pontuacao v] por (1)
  diga [Acertou! Vidro no lugar certo.] por (1) segundos
  transmita [acertou v]
senao
  se <tocando em [Lixo v] ?> entao
    diga [Esse item nao vai no vidro.] por (1) segundos
  fim
fim
```

## Codigo da `Lixeira Metal`
```text
quando este ator for clicado
se <<tocando em [Lixo v] ?> e <(tipoAtual) = [metal]>> entao
  mude [pontuacao v] por (1)
  diga [Acertou! Metal reciclavel.] por (1) segundos
  transmita [acertou v]
senao
  se <tocando em [Lixo v] ?> entao
    diga [Esse item nao vai no metal.] por (1) segundos
  fim
fim
```

## Codigo final do palco
```text
quando eu receber [fim de jogo v]
diga (junte [Fim de jogo! Sua pontuacao foi: ] (pontuacao)) por (4) segundos
```

## Melhorias opcionais
- adicionar sons de acerto e erro;
- criar um botao `Iniciar`;
- usar mais tipos de residuos;
- mostrar curiosidades sobre reciclagem a cada resposta correta.

## Observacao importante
O Scratch nao aceita codigo textual como uma linguagem tradicional. Por isso, este arquivo organiza os blocos em formato de roteiro para voce montar rapidamente no editor.
