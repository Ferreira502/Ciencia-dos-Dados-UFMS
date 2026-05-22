# Feito por Gabriel Ferreira Pereira
# Checkout de Presença e Avaliação da Aprendizagem do Módulo 3 - Entrada, saída de dados e modularização

# funcao para calcular o consumo de combustivel
def calcular_combustivel(distancia, consumo_medio):
    return distancia / consumo_medio

tempo_gasto = int(input())
velocidade_media = int(input())
consumo_medio = int(input())

distancia_percorrida = tempo_gasto * velocidade_media

quantidade_combustivel = calcular_combustivel(distancia_percorrida, consumo_medio)

print(float(quantidade_combustivel))


# Entrada
# 12
# 50
# 15

# Saida Esperada
# 40.0