#Rodrigo Schiavinatto Plassmann
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as conjuntos:
        linhas = conjuntos.readlines()