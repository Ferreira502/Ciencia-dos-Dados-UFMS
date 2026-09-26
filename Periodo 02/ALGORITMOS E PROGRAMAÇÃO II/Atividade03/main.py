# Feito por Gabriel Ferreira Pereira e postado em https://github.com/Ferreira502/Ciencia-dos-Dados-UFMS
# Checkout de Presença e Avaliação da Aprendizagem do Módulo 3 - Estruturas de Dados

fila = []

def enfileirar(elemento):
    fila.append(elemento)
    print(f"'{elemento}' inserido na fila")

def desenfileirar():
    if fila:
        removido = fila.pop(0)
        print(f"'{removido}' removido da fila")
    else:
        print("A fila esta vazia")

def consultar():
    if fila:
        print(f"Inicio da fila: {fila[0]}")
    else:
        print("A fila esta vazia")

def contar():
    print(f"Quantidade de elementos na fila: {len(fila)}")

while True:
    print("\n--- MENU FILA ---")
    print("1 - Enfileirar")
    print("2 - Desenfileirar")
    print("3 - Consultar início")
    print("4 - Contar elementos")
    print("5 - Sair")
    
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        elemento = input("Digite o elemento a inserir: ")
        enfileirar(elemento)
    elif opcao == "2":
        desenfileirar()
    elif opcao == "3":
        consultar()
    elif opcao == "4":
        contar()
    elif opcao == "5":
        print("Programa encerrado")
        break
    else:
        print("Opcao invalida.")