import networkx as nx

def find_solution():
    pass


def add_node(G, tags):
    G.add_node(hash(' '.join(tags)) , {'tags': tags})
    return


def make_graph(photos):
    G = nx.Graph()
    for node in photos['h'] + photos['v']:
        add_node(node)



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
    # print("Case #{}: {}".format(i, find_solution(n, p, tags)))

main()
