#Rodrigo Schiavinatto Plassmann

#Utilização da estrutura with para que o arquivo seja fechado após o uso
#Usando o parâmetro "r", que lê o arquivo
#Arquivo txt armazenado como "conjuntos"
#Utilização do método readline() para que cada linha do texto seja armazenada como elemento de uma lista, nesse caso a lista "linhas"
with open('quatroconjuntos.txt', "r") as conjuntos:
    linhas = conjuntos.readlines()
    
#Variável demonstrando que a primeira linha do arquivo indica a quantidade de operações a serem realizadas
#Utilização do método strip() para remover espaços em branco e pula linhas
#int() usado para converter a string para um número inteiro
qtde_operacoes = int(linhas[0].strip())

#Função que realiza uma operação entre dois conjuntos, com "operacao" indicando a operação que será feita
#No caso do produto cartesiano é utilizada uma função a parte, e não funções já disponibilizadas pelo python como nas outras operações
def realizar_operacoes(operacao, conj1, conj2):
    if operacao == 'U':
        return conj1.union(conj2)
    elif operacao == 'D':
        return conj1.difference(conj2)
    elif operacao == 'I':
        return conj1.intersection(conj2)
    elif operacao == 'C':
        return cart(conj1, conj2)

#Função que faz o produto cartesiano entre dois conjuntos utilizando um loop for dentro de outro for, iterando por todos os elementos de conj1 e conj2
#Os pares ordenados são adicionados na lista "pares_ordenados"
def cart(conj1, conj2):
    pares_ordenados = []
    for i in conj1:
        for j in conj2:
            par_ordenado = (i, j)
            pares_ordenados.append(par_ordenado)
    return pares_ordenados

#contador "i" definido em "1" para começar a contar a partir da segunda linha do arquivo
#loop for que irá iterar baseado na quantidade de operações, contida na primeira linha do arquivo
#conj1 e conj2 são convertidos em conjuntos através do sets, lidos das linhas "i+1" e "i+2"
#strip() remove os espaços em branco e pula linhas
# #split(',') adiciona vírgulas entre os elementos dos conjuntos
# resultado da função "realizar_operacoes é armazenada em "resultado"
# utilização da estrutura "if else" que a partir da operação feita, printa a operação, o conjunto 1, o conjunto 2 e o resultado
# o contador é incrementado em 3, passando pela operação, conjunto 1 e conjunto 2, e chegando a próxima operação e próximos conjuntos
i = 1
for _ in range(qtde_operacoes):
    operacao = linhas[i].strip()
    conj1 = set(linhas[i + 1].strip().split(','))
    conj2 = set(linhas[i + 2].strip().split(','))
    resultado = realizar_operacoes(operacao, conj1, conj2)
    if operacao == 'U':
        print(f'União: conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {resultado}')
    elif operacao == 'D':
        print(f'Diferença: conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {resultado}')
    elif operacao == 'I':
        print(f'Intersecção: conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {resultado}')
    elif operacao == 'C':
        print(f'Produto cartesiano: conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {resultado}')
    else:
        print("Operação inválida")
    i += 3