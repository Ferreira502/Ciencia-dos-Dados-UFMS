# Feito por Gabriel Ferreira Pereira e postado em https://github.com/Ferreira502/Ciencia-dos-Dados-UFMS
# Checkout de Presença e Avaliação da Aprendizagem do Módulo 2 - Variáveis Compostas e Arquivos

import random

numeros = []
pares = []
impares = []

for i in range(100):
    numeros.append(random.randint(1, 1000))

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista original:")
print(numeros)

print("\nLista de números pares:")
print(pares)

print("\nLista de números ímpares:")
print(impares)