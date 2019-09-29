"""
Authors : Kumarage Tharindu & Fan Lei
Class : CSE 472
Organization : ASU CIDSE
Project : SMM Project 1
Task : Friendship Network visualization using NetworkX

"""

import networkx as nx
import matplotlib.pyplot as plt
import data_extraction.data_wrapper as dt


def main():  # main method to execute all the analysis steps
    friendship_network = init_network()

    node_list, edge_list = dt.read_data()  # read the stored edge_graph_csv in data repository

    add_nodes(network=friendship_network, node_list=node_list)  # populate nodes

    add_edges(network=friendship_network, edge_list=edge_list)  # populate edges

    visualize_network(network=friendship_network)


def init_network():  # Initialize a empty NetworkX graph

    init_g = nx.DiGraph(name='Twitter Friendship Network', course='CSE 472')

    return init_g


def add_nodes(network, node_list):  # add list of nodes to a given network

    for node in node_list:
        network.add_node(node, username='John Doe')


def add_edges(network, edge_list): # add list of edges to a given network

    for edge in edge_list:
        network.add_edge(edge[0], edge[1], weight=1)


def visualize_network(network):

    prog_list = ["dot", "sfdp"]

    for prog in prog_list:
        pos = nx.nx_agraph.graphviz_layout(network, prog=prog)
        nx.draw_networkx(network, pos=pos)

        plt.show()


if __name__ == '__main__':
    main()