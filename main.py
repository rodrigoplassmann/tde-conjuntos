#Rodrigo Schiavinatto Plassmann
with open('cincoconjuntos.txt', "r") as conjuntos:
    linhas = conjuntos.readlines()
    
qtde_operacoes = int(linhas[0].strip())

def realizar_operacoes(operacao, conj1, conj2):
    if operacao == 'U':
        return conj1.union(conj2)
    elif operacao == 'D':
        return conj1.difference(conj2)
    elif operacao == 'I':
        return conj1.intersection(conj2)
    elif operacao == 'C':
        return cart(conj1, conj2)

def cart(conj1, conj2):
    pares_ordenados = []
    for i in conj1:
        for j in conj2:
            par_ordenado = (i, j)
            pares_ordenados.append(par_ordenado)
    return pares_ordenados

i = 1
for _ in range(qtde_operacoes):
    operacao = linhas[i].strip()
    conj1 = set(linhas[i + 1].strip().split(','))
    conj2 = set(linhas[i + 2].strip().split(','))
    resultado = realizar_operacoes(operacao, conj1, conj2)
    print(f'{operacao}: conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {resultado}')
    i += 3