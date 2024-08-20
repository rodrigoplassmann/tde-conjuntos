#Rodrigo Schiavinatto Plassmann
def operacoes(operacao, c1, c2):
    if operacao == 'U':
        return c1.union(c2)
    elif operacao == "I":
        return c1.union(c2)
    elif operacao



def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as conjuntos:
        linhas = conjuntos.readlines()
        i = 0
        while i < len(linhas):
            operacao = linhas[i].strip()
ler_arquivo("tresconjuntos.txt")