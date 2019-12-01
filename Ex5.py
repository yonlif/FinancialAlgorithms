import networkx as nx
from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def vcg_cheapest_path(graph, source, target):
    p_price = nx.shortest_path_length(graph, source=source, target=target, weight='weight')
    p = list(pairwise(nx.shortest_path(graph, source=source, target=target, weight='weight')))
    total_pay = 0
    for edge in G.edges:
        if edge not in p:
            print(edge, 0)
            continue
        value = G.adj[edge[0]][edge[1]]['weight']
        _g_without_e = graph.copy()
        _g_without_e.remove_edge(edge[0], edge[1])
        _p_price = nx.shortest_path_length(_g_without_e, source=source, target=target, weight='weight')
        _cost = -value - _p_price + p_price
        print(edge, _cost)
        total_pay += _cost
    print(f"Total {total_pay}")


if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_edge(1, 2, weight=3)
    G.add_edge(1, 3, weight=5)
    G.add_edge(1, 4, weight=10)
    G.add_edge(2, 3, weight=1)
    G.add_edge(2, 4, weight=4)
    G.add_edge(3, 4, weight=1)
    vcg_cheapest_path(G, 1, 4)
    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.plot()
    # plt.show()
