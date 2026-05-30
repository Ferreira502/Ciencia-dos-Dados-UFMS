# Feito por Gabriel Ferreira Pereira e postado em https://github.com/Ferreira502/Ciencia-dos-Dados-UFMS
# Checkout de Presença e Avaliação da Aprendizagem do Módulo 5 - Documentação de programas

# PROGRAMA: Sistema de armazenamento de preços de hortifruti
# DESCRIÇÃO: Este programa simula um sistema de cadastro e
#            consulta de preços de frutas e verduras de um
#            supermercado. Os produtos e seus preços são
#            armazenados em uma única lista de forma
#            intercalada: [produto1, preco1, produto2, preco2, ...]
#            O usuário pode consultar o preço de qualquer
#            produto cadastrado. A busca continua até que o
#            usuário digite a palavra "Fim".



  
#    Função responsável por realizar o cadastro dos produtos e seus preços.

#    Funcionamento:
#        - Lê um número inteiro n, que representa a quantidade de produtos
#          a serem cadastrados.
#        - Para cada produto, lê o nome (string) e o preço (float).
#        - Verifica se o produto já foi cadastrado anteriormente.
#          Se já estiver na lista, exibe a mensagem "Produto já cadastrado"
#          e não realiza a inserção novamente.
#        - Caso contrário, insere o nome do produto e seu preço na lista,
#          de forma intercalada (nome na posição par, preço na posição ímpar).

#    Parâmetros:
#        Nenhum. Os dados são lidos diretamente pelo teclado via input().

#    Retorno:
#        produtos (list): lista contendo os produtos cadastrados e seus
#                         respectivos preços, no formato:
#                         [produto1, preco1, produto2, preco2, ...]
  

def cadastrar_produtos():

    # Cria uma lista vazia que irá armazenar os produtos e seus preços
    produtos = []

    # Lê a quantidade de produtos que serão cadastrados
    n = int(input())

    # Repete o processo de leitura n vezes, uma para cada produto
    for i in range(n):

        # Lê o nome do produto digitado pelo usuário
        produto = input()

        # Lê o preço do produto e converte para número decimal (float)
        preco = float(input())

        # Verifica se o produto já está presente na lista
        # O operador "in" percorre todos os elementos da lista em busca do nome
        if produto in produtos:
            # Informa ao usuário que o produto já foi cadastrado anteriormente
            print("Produto já cadastrado")

        else:
            # Adiciona o nome do produto ao final da lista
            produtos.append(produto)

            # Adiciona o preço do produto logo em seguida,
            # mantendo a estrutura intercalada [nome, preco, nome, preco, ...]
            produtos.append(preco)

    # Retorna a lista completa com todos os produtos cadastrados
    return produtos


    # Função responsável por buscar o preço de um produto na lista de cadastros.

    # Funcionamento:
    #     - Percorre a lista de produtos de dois em dois índices (0, 2, 4, ...),
    #       pois os nomes estão sempre nas posições pares e os preços nas
    #       posições ímpares imediatamente seguintes.
    #     - Se o nome do produto for encontrado na posição i, retorna o preço
    #       armazenado na posição i+1.
    #     - Caso o produto não seja encontrado após percorrer toda a lista,
    #       retorna a mensagem "Produto não cadastrado".

    # Parâmetros:
    #     produtos (list): lista com os produtos e preços cadastrados,
    #                      no formato [produto1, preco1, produto2, preco2, ...]
    #     produto (str):   nome do produto a ser pesquisado.

    # Retorno:
    #     - O preço (float) do produto, caso ele esteja cadastrado.
    #     - A string "Produto não cadastrado", caso contrário.
    # 

def buscar_preco(produtos, produto):

    # Percorre a lista pulando de dois em dois índices (posições dos nomes)
    for i in range(0, len(produtos), 2):

        # Compara o nome armazenado na posição i com o produto buscado
        if produtos[i] == produto:

            # Retorna o preço que está na posição seguinte (i + 1)
            return produtos[i + 1]

    # Se o laço terminar sem encontrar o produto, retorna mensagem de aviso
    return "Produto não cadastrado"


# BLOCO PRINCIPAL DO PROGRAMA

# Chama a função de cadastro e armazena a lista de produtos retornada
produtos = cadastrar_produtos()

# Lê o primeiro nome de produto a ser consultado
nome = input()

# Continua consultando enquanto o usuário não digitar "Fim"
# Atenção: Python diferencia maiúsculas de minúsculas, então
# "fim", "FIM" e "Fim" são considerados valores diferentes
while nome != "Fim":

    # Busca e imprime o preço do produto digitado (ou mensagem de erro)
    print(buscar_preco(produtos, nome))

    # Lê o próximo nome a ser consultado
    nome = input()

# Quando o usuário digita "Fim", o laço encerra e o programa termina


# COMPLEXIDADE GERAL DO PROGRAMA:
#   Sendo n = número de produtos cadastrados e
#          q = número de consultas realizadas pelo usuário:
#
#   - Tempo:  O(n² + q·n)
#       * O cadastro é O(n²) pois, para cada um dos n produtos,
#         o operador "in" faz uma busca linear na lista (O(n)),
#         resultando em n × n = n² comparações no pior caso.
#       * Cada uma das q consultas executa buscar_preco(), que
#         é O(n) no pior caso (percorre toda a lista).
#       * Total: O(n²) + O(q·n) = O(n² + q·n).
#
#   - Espaço: O(n)
#       * A lista armazena exatamente 2·n elementos
#         (um nome e um preço por produto), crescendo
#         linearmente com o número de produtos cadastrados.


# EXEMPLOS DE EXECUÇÃO

# Exemplo 1:
# Entrada:
# 2
# laranja
# 3.80
# maça
# 6.40
# laranja
# Saída:
# 3.8

# Exemplo 2:
# Entrada:
# 1
# pera
# 3.80
# Fim
# Saída:
# 