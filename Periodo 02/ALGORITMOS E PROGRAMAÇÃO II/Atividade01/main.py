# Feito por Gabriel Ferreira Pereira e postado em https://github.com/Ferreira502/Ciencia-dos-Dados-UFMS
# Checkout de Presença e Avaliação da Aprendizagem do Módulo 1 - Variáveis Compostas e Arquivos


arquivo_entrada = input("Informe o nome do arquivo de entrada: ")
arquivo_saida = input("Informe o nome do arquivo de saida: ")

substituicoes = {
    "a": "!",
    "e": "@",
    "i": "#",
    "o": "$",
    "u": "%",
}

with open(arquivo_entrada, "r", encoding="utf-8") as entrada:
    conteudo = entrada.read()

texto_codificado = ""

for caractere in conteudo:
    letra_minuscula = caractere.lower()

    if letra_minuscula in substituicoes:
        texto_codificado += substituicoes[letra_minuscula]
    else:
        texto_codificado += caractere

with open(arquivo_saida, "w", encoding="utf-8") as saida:
    saida.write(texto_codificado)

print("Conversao concluida")
