import networkx as nx
import matplotlib.pyplot as plt
import pickle



def create_nodes(G,adj_dict):
    for key in adj_dict.keys():
        if G.has_node(key):
            continue
        else:
            G.add_node(key,s_v = 0)
    return G
    #print(G.order())

    '''nx.draw(G,with_labels=True)
    plt.draw()
    plt.show()'''




def create_edges(G1,adj_dict):
    for key in adj_dict.keys():
        for out_node in adj_dict[key]:
            if out_node in adj_dict.keys() and out_node!=key:        #avoided self loop
                if G1.has_node(key) and G1.has_node(out_node):
                    if not G1.has_edge(key,out_node):
                        G1.add_edges_from([(key,out_node)])

    pr = nx.pagerank(G1,alpha=0.85)
    print(pr)






def create_adj_graph():
    pickle_in = open("adj_link_list.pickle","rb")
    adj_dict = pickle.load(pickle_in)
    G = nx.DiGraph()
    G1 = create_nodes(G,adj_dict)
    create_edges(G1,adj_dict)




def main():
    create_adj_graph()

    #print(adj_dict)

if __name__ == '__main__':
    main()



'''

G = nx.DiGraph()

G.add_node(1)
G.add_node(2)

G.add_edges_from([(1,2)])

print(G.has_edge(1, 2))


nx.draw(G,with_labels=True)
plt.draw()
plt.show()
'''
