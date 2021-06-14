"""
    pair        dist     path
  1 →   2     4       1 → 2
  1 →   3     8       1 → 3
  1 →   4    15       1 → 4
  1 →   5    21       1 → 4 → 5
  2 →   1     4       2 → 1
  2 →   3    12       2 → 1 → 3
  2 →   4    15       2 → 4
  2 →   5    20       2 → 5
  3 →   1     8       3 → 1
  3 →   2    12       3 → 1 → 2
  3 →   4     8       3 → 4
  3 →   5    14       3 → 5
  4 →   1    15       4 → 1
  4 →   2    15       4 → 2
  4 →   3     8       4 → 3
  4 →   5     6       4 → 5
  5 →   1    21       5 → 4 → 1
  5 →   2    20       5 → 2
  5 →   3    14       5 → 3
  5 →   4     6       5 → 4
"""

from itertools import permutations

"""
# Obtem todas as permutações
#perm = permutations(['a', 'b', 'c', 'd', 'e']
perm = permutations([1, 2, 3, 4, 5])

#list = []

cont = 0

# Imprime as permutações
for i in list(perm):
    cont = cont + 1
    print(f'{cont} -> {i}')
    #aux1 = i[0], i[1], i[2], i[3], [4]
    #list.append(aux1)

qntd = len([perm])

print(f'Olá, A quantidade = {qntd}')
"""



"""
qntd = int(input("Insira a quantidade de alunos: "))

print(f'Olá, quantidade = {qntd}')

i = int(((qntd * qntd) - qntd)/2)
print(f'Existem {i} interacoes')

for origem in range (1, qntd + 1) :

    for proximo in range (1, qntd + 1) :
        if origem != proximo and origem < proximo:
            peso = int(input(f'({origem},{proximo}) - Insira o peso da rota: '))
            print(f'{origem} → {proximo} = {peso} && {proximo} → {origem} = {peso}')

            g.adiciona_aresta(origem, proximo, peso)
            g.adiciona_aresta(proximo, origem, peso)


g.mostra_matriz()

resultado_dijkstra = g.dijkstra(1)
print(resultado_dijkstra)
"""



from math import inf
from itertools import product


def floyd_warshall(n, edge):
    rn = range(n)

    matriz = []
    matriz2 = []
    valor = []

    dist = [[inf] * n for i in rn]
    nxt = [[0] * n for i in rn]

    for i in rn:
        dist[i][i] = 0

    for u, v, w in edge:
        dist[u - 1][v - 1] = w
        nxt[u - 1][v - 1] = v - 1


    #Printa todas as diastancias entre todos os pontos
    print("    pair        dist     path")
    for i, j in product(rn, repeat=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(nxt[path[-1]][j])
            print("%3d → %3d  %4d       %s"
                  % (i + 1, j + 1, dist[i][j],
                     ' → '.join(str(p + 1) for p in path)))


            aux = i+1, j+1, dist[i][j]
            matriz.append(aux)
    """
    for i in i+1:
        for j in j+1:
            matriz
    """
    print(f'\nmatriz: {matriz}')

    cont = 0

    perm = permutations([1, 2, 3, 4, 5])
    for i in list(perm):
        cont = cont + 1
        print(f'{cont} -> {i}')
        print(f'posicao {cont} ')
        for x in range(1, 120):
            for y in range (0,5):
                print(f"posicao x: {i[y]} & posicao y: {i[x]}")




if __name__ == '__main__':
    floyd_warshall(5, [
        [1, 2, 4],
        [1, 3, 8],
        [1, 4, 15],
        [1, 5, 24],
        [2, 1, 4],
        [2, 3, 300],
        [2, 4, 15],
        [2, 5, 20],
        [3, 1, 8],
        [3, 2, 300],
        [3, 4, 8],
        [3, 5, 14],
        [4, 1, 15],
        [4, 2, 15],
        [4, 3, 8],
        [4, 5, 6],
        [5, 1, 24],
        [5, 2, 20],
        [5, 3, 14],
        [5, 4, 6]])

"""
    floyd_warshall(5, [
        ['a', 'b', 4],
        ['a', 'c', 8],
        ['a', 'd', 15],
        ['a', 'e', 24],
        ['b', 'a', 4],
        ['b', 'c', 300],
        ['b', 'd', 15],
        ['b', 'e', 20],
        ['c', 'a', 8],
        ['c', 'b', 300],
        ['c', 'd', 8],
        ['c', 'e', 'a'],
        ['d', 'a', 15],
        ['d', 'b', 15],
        ['d', 'c', 8],
        ['d', 'e', 6],
        ['e', 'a', 24],
        ['e', 'b', 20],
        ['e', 'c', 14],
        ['e', 'd', 6]])
"""






"""
    lista = prim
    matriz = []

    for palavra in lista:
        matriz.append(list(palavra))

    print(f'\n --> matriz {matriz}')

    print(f'\n --> prim {lista}')

    string = str(matriz[0])
    string2 = str(matriz[3])

    result = list(string)
    result2 = list(string2)

    print(f'\n --> Primeiro {result[7]}')
    print(f'\n --> Ultimo {result2[7]}')
"""

