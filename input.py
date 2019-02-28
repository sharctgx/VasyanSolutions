import networkx as nx
from networkx.algorithms.distance_measures import diameter

def find_solution():
    pass


def count_interest(a, b):
    one = len(set(a['tags']) & set(b['tags']))
    two = len(set(a['tags']) - set(b['tags']))
    three = len(set(b['tags']) - set(a['tags']))
    return min([one, two, three])


def add_node(G, tags, orient):
    G.add_node(hash(' '.join(tags)), tags=tags, orient=orient)
    return


def add_edge(G, a, b):
    G.add_edge(a[0], b[0], weight=0-count_interest(a[1], b[1]))
    return


def make_graph(photos):
    G = nx.Graph()
    for tags in photos['h']:
        add_node(G, tags, 'h')
    for tags in photos['v']:
        add_node(G, tags, 'v')
    return G


def get_sorted_edges(G):
    edges = []
    nodes = list(G.nodes(data=True))
    for x in range(len(nodes)):
        for y in range(x, len(nodes)):
            edges.append((nodes[x], nodes[y], count_interest(nodes[x][1], nodes[y][1])))
    return sorted(edges, key=lambda x: x[2], reverse=True)


def add_sorted_edges(G, edges):
    for edge in edges:
        add_edge(G, *[x[0] for x in edge])
        if nx.find_cycle(G):
            G.remove_edge(*[x[0] for x in edge])
    return


def read_input():
    t = int(input())
    photos = list()
    for i in range(1, t + 1):
        orient, num, tags = [x for x in input().split(' ', 2)]
        tags = tags.split()
        if orient == 'H':
            photos.append({"num" : i, "is_horizontal" : True, "tags" : tags})
        else:
            photos.append({"num" : i, "is_horizontal" : False, "tags" : tags})
    return photos


def main():
    photos = read_input()
    G = make_graph(photos)
    edges = get_sorted_edges(G)
    diameter

main()
