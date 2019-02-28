import networkx as nx
import make_pairs

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

    # print(make_pairs.make_pairs_hash_table(photos))
    # G = make_graph(photos)

main()
