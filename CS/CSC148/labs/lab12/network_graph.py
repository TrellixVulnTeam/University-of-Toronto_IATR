import networkx as nx
import random

def page_rank():
    """Return top 10 node

    @rtype: list
    """
    graph = nx.Graph()

    with open('facebook-links.txt', 'r') as f:
        for line in f:
            s = line.split('\t')
            graph.add_edge(int(s[0]), int(s[1]))

    assert len(graph.nodes()) == 63731
    assert len(graph.edges()) == 817090

    g = graph.subgraph(range(10000)) # take a subset of the graph for speed


    #set initial cur node
    node_list = g.nodes()
    cur_node_index = random.randint(0, 9999)
    cur_node = node_list[cur_node_index]


    for i in range(10000):
        p_value = random.randint(1, 10)
        if p_value != 1:
            cur_neighbor_list = g.neighbors(cur_node)
            cur_node = cur_neighbor_list[random.randint(0, len(cur_neighbor_list)-1)]
            if g.node[cur_node] == {}:
                g.node[cur_node]['acc'] = 1
            else:
                g.node[cur_node]['acc'] += 1
        else:
            cur_node_index = random.randint(0, 9999)
            cur_node = node_list[cur_node_index]
            if g.node[cur_node] == {}:
                g.node[cur_node]['acc'] = 1
            else:
                g.node[cur_node]['acc'] += 1

    target = g.nodes(data=True)
    acc_node_list = [(x[1]['acc'], x[0]) for x in target if 'acc' in x[1]]
    acc_node_list.sort()
    res = acc_node_list[::-1][:10]
    return res

if __name__ == "__main__":
    res = page_rank()
    print(res)
