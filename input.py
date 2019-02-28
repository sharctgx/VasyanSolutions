import networkx as nx
import make_pairs
from networkx.algorithms.distance_measures import diameter
from pprint import pprint

def find_solution():
    pass


def count_interest(a, b):
    one = len(set(a['tags']) & set(b['tags']))
    two = len(set(a['tags']) - set(b['tags']))
    three = len(set(b['tags']) - set(a['tags']))
    return min([one, two, three])


def add_node(G, photo):
    G.add_node(photo['num'], tags=photo['tags'], orient=photo['is_horizontal'])
    return


def add_edge(G, a, b, weight=1):
    G.add_edge(a, b, weight=0-weight)
    return


def make_graph(photos):
    G = nx.Graph()
    for photo in photos:
        add_node(G, photo)
    return G


def get_sorted_edges(G):
    edges = []
    nodes = list(G.nodes(data=True))
    for x in range(len(nodes)):
        for y in range(x+1, len(nodes)):
            edges.append((nodes[x], nodes[y], count_interest(nodes[x][1], nodes[y][1])))
    return sorted(edges, key=lambda x: x[2], reverse=True)


def add_sorted_edges(G, edges, f):
    for edge in edges:
        add_edge(G, *[x[0] for x in edge[:2]], weight=edge[-1])
        try:
            nx.find_cycle(G)
            G.remove_edge(*[x[0] for x in edge[:2]])
        except:
            if G.degree(edge[0][0]) > 2 or G.degree(edge[1][0]) > 2:
                G.remove_edge(*[x[0] for x in edge[:2]])
            else:
                continue
    return


def read_input():
    t = int(input())
    photos = list()
    for i in range(0, t):
        orient, num, tags = [x for x in input().split(' ', 2)]
        tags = tags.split()
        if orient == 'H':
            photos.append({"num" : i, "is_horizontal" : True, "tags" : set(tags)})
        else:
            photos.append({"num" : i, "is_horizontal" : False, "tags" : set(tags)})
    return photos


def main():
    photos = read_input()
    G = make_graph(photos)
    n = len(G.nodes())
    # print(n*(n-1)/2)
    # pprint(G.nodes(data=True))
    edges = get_sorted_edges(G)
    # for edge in edges:
    #     print(edge)
    with open('out.txt', 'w') as f:
        add_sorted_edges(G, edges, f)
    # pprint(G.edges())
    dia = diameter(G)
    print(dia)

main()
