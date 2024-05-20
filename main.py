import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
graf = [
    {
        'i': 1,
        'j': 2,
        't': 9
    },
    {
        'i': 1,
        'j': 3,
        't': 5
    },
    {
        'i': 1,
        'j': 4,
        't': 8
    },
    {
        'i': 2,
        'j': 5,
        't': 4,
    },
    {
        'i': 3,
        'j': 4,
        't': 12
    },
    {
        'i': 4,
        'j': 5,
        't': 3
    }
]
costs = {}
costsMax = {
}
nc = {}
processed = []
parents = {}


def create_graf():
    nodes = []
    edges = []
    for i in graf:
        if nodes.__contains__(i['i']) is False:
            nodes.append(i['i'])
        if nodes.__contains__(i['j']) is False:
            nodes.append(i['j'])
        edges.append((i['i'], i['j']))
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


def process_data():
    print('')


def base_prepare():
    inf = float('inf')
    for i in get_nodes():
        nc[i] = []
        costs[i] = inf


def get_nodes():
    nodes = []
    for i in graf:
        if nodes.__contains__(i['i']) is False:
            nodes.append(i['i'])
        if nodes.__contains__(i['j']) is False:
            nodes.append(i['j'])
    return nodes


def set_nc():
    for g in graf:
        nc[g['i']].append(g['j'])


def base_costs():
    node = nc[1]
    for n in node:
        costs[n] = next(i for i in graf if i['j'] == n)['t']


def get_lower_cost(costs_current):
    lower_cost = float('inf')
    lower_node = None
    for c in costs:
        if costs_current[c] < lower_cost and c not in processed:
            lower_cost = costs_current[c]
            lower_node = c
    return lower_node


def get_max_cost(costs_current):
    lower_cost = 0
    lower_node = None
    for c in costs:
        if costs_current[c] > lower_cost and c not in processed:
            lower_cost = costs_current[c]
            lower_node = c
    return lower_node


def get_min_way():
    node = get_lower_cost(costs)
    while node is not None:
        cost = costs[node]
        neighbors = nc[node]
        for n in neighbors:
            new_cost = cost + next(i for i in graf if i['j'] == n and i['i'] == node)['t']
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = get_lower_cost(costs)


def get_max_way(node):
    cost = costsMax.get(node['i'], 0) + node['t']
    if cost > costsMax.get(node['j'], 0):
        costsMax[node['j']] = cost
    for g in [i for i in graf if i['i'] == node['j']]:
        get_max_way(g)


def show_data():
    value = list(costsMax.items())
    value.sort(key=lambda x: x[0], reverse=False)
    print('max way', value)
    print('parents', parents)
    print('edges', nc)
    create_graf()


def main():
    base_prepare()
    set_nc()
    base_costs()
    get_min_way()
    get_max_way({'i': 0, 'j': 1, 't': 0})
    show_data()


if __name__ == "__main__":
    main()
