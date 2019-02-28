import networkx as nx

def find_solution():
    pass


def count_interest(a, b):
    one = len(set(a['tags']) & set(b['tags']))
    two = len(set(a['tags']) - set(b['tags']))
    three = len(set(b['tags']) - set(a['tags']))
    return min([one, two, three])


def add_node(G, tags, orient):
    G.add_node(hash(' '.join(tags)), tags= tags, orient= orient)
    return


def add_edge(G, a, b):
    G.add_edge(hash(a[0]), hash(b[0]), weight=0-count_interest(a[1], b[1]))
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


def main():
    t = int(input())
    photos = {'v': [], 'h': []}
    for i in range(1, t + 1):
        orient, num, tags = [x for x in input().split(' ', 2)]
        tags = tags.split()
        if orient == 'H':
            photos['h'].append(tags)
        else:
            photos['v'].append(tags)
    G = make_graph(photos)
    print(get_sorted_edges(G))
    # print("Case #{}: {}".format(i, find_solution(n, p, tags)))

main()
