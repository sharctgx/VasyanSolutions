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


def read_input():
    t = int(input())
    photos = list()
    for i in range(1, t + 1):
        orient, num, tags = [x for x in input().split(' ', 2)]
        tags = tags.split()
        if orient == 'H':
            photos.append(tuple(i, 'h', tags))
        else:
            photos.append(tuple(i, 'v', tags))
    return photos


def main():
    photos = read_input()
    G = make_graph(photos)

main()
