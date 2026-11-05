# Feito por Gabriel Ferreira Pereira e postado em https://github.com/Ferreira502/Ciencia-dos-Dados-UFMS
# Checkout de Presença e Avaliação da Aprendizagem do Módulo 4 - Noções de Eficiência e Recursividade

def somar_naturais(n):
    if n == 0:
        return 0
    return n + somar_naturais(n - 1)


numero = int(input("Digite um numero inteiro positivo: "))

if numero > 0:
    print("Resultado da soma:", somar_naturais(numero))
else:
    print("O numero deve ser positivo")
