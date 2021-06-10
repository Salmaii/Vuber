from Graph import Graph
import networkx as nx
import statistics
import matplotlib.pyplot as plt
from random import randint


# Implementacao baseada no exemplo disponivel em:
# https://networkx.readthedocs.io/en/stable/examples/drawing/weighted_graph.html
def print_graph(g, save_png=False):
    nxg = nx.Graph()
    costs = []
    for (a, b, cost) in g.edges():
        nxg.add_edge(a, b, cost=cost)
        costs.append(cost)

    pos = nx.spring_layout(nxg)  # positions for all nodes

    avg_cost = statistics.mean(costs)

    elarge = [(u, v) for (u, v, d) in nxg.edges(data=True) if d['cost'] > avg_cost]
    esmall = [(u, v) for (u, v, d) in nxg.edges(data=True) if d['cost'] <= avg_cost]

    # nodes
    nx.draw_networkx_nodes(nxg, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(nxg, pos, edgelist=elarge, width=4)
    nx.draw_networkx_edges(nxg, pos, edgelist=esmall, width=4, alpha=0.5, edge_color='b', style='dashed')

    # labels
    nx.draw_networkx_labels(nxg, pos, font_size=20, font_family='sans-serif')
    nx.draw_networkx_edge_labels(nxg, pos)

    plt.axis('off')
    if save_png:
        plt.savefig("graph.png")  # save as png

    plt.show()  # display


def first_edge(g, save_png=False):
    nxg = nx.Graph()
    costs = []
    for (a, b, cost) in g.edges():
        nxg.add_edge(a, b, cost=cost)
        costs.append(cost)

    pos = nx.spring_layout(nxg)  # positions for all nodes

    avg_cost = statistics.mean(costs)

    elarge = [(u, v) for (u, v, d) in nxg.edges(data=True) if d['cost'] > avg_cost]
    esmall = [(u, v) for (u, v, d) in nxg.edges(data=True) if d['cost'] <= avg_cost]

    # nodes
    nx.draw_networkx_nodes(nxg, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(nxg, pos, edgelist=elarge, width=4)
    nx.draw_networkx_edges(nxg, pos, edgelist=esmall, width=4, alpha=0.5, edge_color='b', style='dashed')

    # labels
    nx.draw_networkx_labels(nxg, pos, font_size=20, font_family='sans-serif')
    nx.draw_networkx_edge_labels(nxg, pos)

    plt.axis('off')
    if save_png:
        plt.savefig("graph.png")  # save as png

    plt.show()  # display



def generate_random_graph(nodes, max_cost=20):

    l = len(nodes)
    _g = Graph({})

    for i in range(l):
        r1 = randint(1, l - 1)
        r2 = randint(1, l - 1)

        n1 = nodes[i]
        n2 = nodes[(i + r1) % l]
        n3 = nodes[(i + r2) % l]

        _g.add_edge(n1, n2, randint(1, max_cost))
        _g.add_edge(n1, n3, randint(1, max_cost))

    return _g

"""
def generate_graph(nodes, max_cost=20):

    l = len(nodes)
    _g = Graph({})

    for i in range(l):
        r1 = randint(1, l - 1)
        r2 = randint(1, l - 1)

        n1 = nodes[i]
        n2 = nodes[(i + r1) % l]
        n3 = nodes[(i + r2) % l]

        _g.add_edge(n1, n2, randint(1, max_cost))
        _g.add_edge(n1, n3, randint(1, max_cost))

    return _g
"""

if __name__ == '__main__':

    g = Graph({})

    edges = [
        ('a', 'b', 4), ('a', 'c', 8), ('a', 'd', 15), ('a', 'e', 24),
        ('b', 'c', 30), ('b', 'd', 15), ('b', 'e', 20),
        ('c', 'd', 8), ('c', 'e', 14),
        ('d', 'e', 6)]
    for e in edges:
        g.add_edge(*e)

    print(g)
    print_graph(g)

'''

    - Funcao do vertice original
    g = Graph({})
    edges = [('a', 'b', 17), ('a', 'e', 14), ('a', 'h', 5), ('b', 'g', 18), ('b', 'h', 13), ('c', 'e', 20),
            ('c', 'f', 2), ('d', 'e', 19), ('d', 'g', 8), ('e', 'g', 12), ('f', 'g', 1), ('f', 'h', 13)]
    for e in edges:
        g.add_edge(*e)
    
    
    - Vertices aleatorios
    #g = generate_graph('abcde')
    #g = generate_random_graph('123456789')
    
    
    - Vertices originais
    edges = [('a', 'b', 17), ('a', 'e', 14), ('a', 'h', 5), ('b', 'g', 18), ('b', 'h', 13), ('c', 'e', 20),
            ('c', 'f', 2), ('d', 'e', 19), ('d', 'g', 8), ('e', 'g', 12), ('f', 'g', 1), ('f', 'h', 13)]
          
            
    - Vertices completos  
    edges = [
        ('a', 'b', 4), ('a', 'c', 8), ('a', 'd', 15), ('a', 'e', 24),
        ('b', 'a', 4), ('b', 'c', 300), ('b', 'd', 15), ('b', 'e', 20),
        ('c', 'a', 8), ('c', 'b', 300), ('c', 'd', 8), ('c', 'e', 14),
        ('d', 'a', 15), ('d', 'b', 15), ('d', 'c', 8), ('d', 'e', 6),
        ('e', 'a', 24), ('e', 'b', 20), ('e', 'c', 14), ('e', 'd', 6),
    ]

'''

