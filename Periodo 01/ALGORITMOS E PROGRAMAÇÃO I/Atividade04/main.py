# Feito por Gabriel Ferreira Pereira e postado em https://github.com/Ferreira502/Ciencia-dos-Dados-UFMS
# Checkout de Presença e Avaliação da Aprendizagem do Módulo 4 - Estruturas de programação

# funcao para cadastrar produtos
def cadastrar_produtos():
    produtos = {}

    n = int(input())

    for i in range(n):
        produto = input()
        preco = float(input())

        if produto in produtos:
            print("Produto ja cadastrado")
        else:
            produtos[produto] = preco

    return produtos


def buscar_preco(produtos, produto):
    if produto in produtos:
        return produtos[produto]

    return "Produto nao cadastrado"


produtos = cadastrar_produtos()

nome = input()

while nome != "Fim":
    print(buscar_preco(produtos, nome))

    nome = input()

# Exemplo 1:
# Entrada
# 2
# laranja
# 3.80
# maça
# 6.40
# laranja
# Saida
# 3.8

# Exemplo 2:
# Entrada
# 1
# pera
# 3.80
# Fim
# Saida
#