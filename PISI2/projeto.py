arquivo = open("PISI/mapa.txt")
# Buscando do arquivo a primeira linha para as dimensões e a linhas para montar a matriz
dimensoes = [int(x) for x in arquivo.readline().split()]
matriz = []
for l in range(dimensoes[0]):
    linha = []
    linha = arquivo.readline().split()
    matriz += [linha]
print(dimensoes)
print(matriz)

# Verificando os valores da matriz
pontos = []
letras = []
for x in range(dimensoes[0]):
    for y in range(dimensoes[1]):
        if matriz[x][y] == "R":  # Definindo o valor de partida
            inicio = [x, y]
        elif matriz[x][y] != "0" and matriz[x][y] != "R":
            pontos.append([x, y])  # Guardadando o par coordenado da letra
            letras.append(matriz[x][y])  # Guardando a letra correspondente


def gerar_permutacoes(lista):
    # Caso base: se a lista tiver apenas um elemento, retorna uma lista contendo esse elemento
    if len(lista) == 1:
        return [lista]

    permutacoes = []  # Lista para armazenar as permutações

    # Iterar sobre cada elemento da lista
    for i, elemento in enumerate(lista):
        # Gerar permutações para a lista sem o elemento atual
        sem_elemento_atual = lista[:i] + lista[i + 1 :]
        permutacoes_sem_elemento_atual = gerar_permutacoes(sem_elemento_atual)

        # Adicionar o elemento atual a todas as permutações geradas
        for permutacao in permutacoes_sem_elemento_atual:
            permutacoes.append([elemento] + permutacao)

    return permutacoes


opcoes = gerar_permutacoes(pontos)  # Gerando todas as opções com os pontos
caminhos = gerar_permutacoes(letras)  # Gerando todas as opções com as letras


matriz = []
for x in opcoes:
    x.insert(0, inicio)  # Inserindo o ponto inicial
    x.append(inicio)  # Inserindo o ponto final
    matriz += [x]

# Fazendo o cálculo para encontrar a distância total de cada um dos caminhos existentes
distancias = []
for linha in matriz:
    distancia = 0
    for i in range(len(linha) - 1):
        result = abs(linha[i][0] - linha[i + 1][0]) + abs(
            linha[i][1] - linha[i + 1][1]
        )  # Calculo que soma os valores absolutos depois de substrair os pontos correspondentes
        distancia += result  # Calculando o percurso total da permutação da vez
    distancias.append(distancia)  # Guardando todos os valores de distância a uma lista

# Fazendo as listas unidas virarem uma tupla
tuplas = list(zip(caminhos, distancias))

# Transformando as listas em tuplas
dicionario = {}
for caminhos, distancias in tuplas:
    dicionario[tuple(tuple(ponto) for ponto in caminhos)] = distancias


menor = dicionario[
    min(dicionario, key=dicionario.get)
]  # Encontrando o menor valor no dicionário


# Função que encontra a chave correspondente ao menor valor
def encontrar_chave(dicionario, valor):
    for chave, val in dicionario.items():
        if val == valor:
            return chave
    return None


dicionario = encontrar_chave(dicionario, menor)

print(dicionario)
