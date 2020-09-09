import pickle
import requests
import networkx as nx
import matplotlib.pyplot as plt


def page_rank():
    G = nx.DiGraph()
    pickle_in = open("network.pickle","rb")
    G = pickle.load(pickle_in)
    num_node = G.number_of_nodes()
    for node,degree in G.out_degree():
        G.nodes[node]['s_v'] = 1/num_node

    epsilon = 0.15

    for i in range(100):
        dict_inter = {}
        for destination,degree in G.out_degree():
            sum = 0
            for source_node,destination_node in G.in_edges(destination):
                sum = sum + (G.nodes[source_node]['s_v']/G.out_degree(source_node))
            dict_inter[destination] = (epsilon/num_node) + ((1 - epsilon)* sum)

        for key in dict_inter.keys():
            G.nodes[key]['s_v'] = dict_inter[key]

    page_rank_dict = {}
    for node,degree in G.out_degree():
        page_rank_dict[node] = G.nodes[node]['s_v']
    pickle_out = open("page_rank.pickle","wb")
    pickle.dump(page_rank_dict, pickle_out)
    pickle_out.close()
