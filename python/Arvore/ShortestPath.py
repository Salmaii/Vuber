from Graph import Graph
from queue import PriorityQueue
from math import inf


def dijkstra(graph, root):

    queue = PriorityQueue()  # Lista de prioridades

    path = {}  # Dicionário com o caminho e o custo total
    for v in graph.vertices():
        if v == root:
            path[v] = [[], 0]  # Custo 0 para o root
        else:
            path[v] = [[], inf]  # Custo infinito para os demais

        queue.put((path[v][1], v))  # Adiciona todas na lista de prioridade (maior prioridade = menor custo)

    remaing_vertices = list(graph.vertices())  # lista de vertices nao visitados

    for i in range(len(graph.vertices())):
        u = queue.get()[1]  # vertice prioritario da lista
        remaing_vertices.remove(u)  # remove da lista de nao visitados

        for v in remaing_vertices:  # para cada v nao visitado
            du = path[u][1]  # menor custo ate vertice u (prioritario)
            w = graph.direct_cost(u, v)  # custo de u ate v
            dv = path[v][1]  # menor custo ate vertice v
            if du + w < dv:  # O caminho até v pelo u é menos custoso que o melhor até então?
                path[v][1] = du + w  # Atualiza o custo
                path[v][0] = path[u][0] + [u]  # Atualiza o caminho
                queue.queue.remove((dv, v))  # Atualiza a prioridade do vertice v na lista de prioridade
                queue.put((path[v][1], v))

    return path


def path_as_string(path):
    path_tidy = []
    vertices = sorted(path.keys())
    for v in vertices:
        cost = path[v][1]
        if cost == 0:
            continue
        p = '-'.join(path[v][0]) + '-' + v
        path_tidy.append(p + ' custo: ' + str(cost))
    return '\n'.join(path_tidy)


def prim(graph, root):
    vertex = [root]  # Lista dos vertices a partir do qual buscamos as arestas
    selected_edges = []  # Lista com as arestas selecionadas

    weight = 0  # Peso do minimum spanning tree

    remaing_vertices = list(graph.vertices())  # Lista com os vertices destinos da busca
    remaing_vertices.remove(root)  # O root eh ponto de partida, entao sai da lista

    for i in range(len(remaing_vertices)):  # Devemos buscar |V| - 1 vertices
        min_cost = inf  # Inicializamos o custo minimo como infinito
        va, vb = None, None  # Vertices candidatos para a aresta selecionada
        for v1 in vertex:  # Para cada vertice na lista de busca origem
            for v2 in remaing_vertices:  # Buscamos os vertices que ainda nao estao no grafo final
                cost = graph.direct_cost(v1, v2)  # Calcula o custo da aresta
                if cost < min_cost:  # Se for menor que o minimo ate entao, atualizamos os dados
                    va = v1
                    vb = v2
                    min_cost = cost

        if min_cost < inf:  # Depois de todas as buscas, se o custo eh finito:
            selected_edges.append((va, vb, min_cost))  # Adicionamos a aresta de va a vb na solucao
            vertex.append(vb)  # vb agora sera nova origem de busca
            remaing_vertices.remove(vb)  # vb nao mais sera destino de busca, pois ja consta na solucao
            weight += min_cost  # Atualiza o peso


    return selected_edges, weight  # Retorna a lista de arestas selecionadas com o peso total


if __name__ == '__main__':

    g = Graph({})
    edges = [
        ('a', 'b', 4), ('a', 'c', 8), ('a', 'd', 15), ('a', 'e', 24),
        ('b', 'c', 30), ('b', 'd', 15), ('b', 'e', 20),
        ('c', 'd', 8), ('c', 'e', 14),
        ('d', 'e', 6)]
    #edges = [('a', 'b', 17), ('a', 'e', 14), ('a', 'h', 5), ('b', 'g', 18), ('b', 'h', 13), ('c', 'e', 20),
    #        ('c', 'f', 2), ('d', 'e', 19), ('d', 'g', 8), ('e', 'g', 12), ('f', 'g', 1), ('f', 'h', 13)]
    for e in edges:
        g.add_edge(*e)
    g_prim = Graph({})
    prim, w = prim(g, 'a')  # Retorna as arestas e o peso
    for e in prim:
        g_prim.add_edge(*e)

    print('Grafo Original:\n%s' % g)
    print('--')
    print('Caminhos mais curtos desde o vertice \'a\':\n%s' % path_as_string(dijkstra(g, 'a')))
    print('--')
    print('Minimal Spanning Tree (Peso Final = %s):\n%s' % (w, g_prim))

    """
    from machine_learning_class.GraphUtils import print_graph
    print_graph(g)
    print_graph(g_prim)
    """
