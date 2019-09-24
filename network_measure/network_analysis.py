"""
Authors : Kumarage Tharindu & Fan Lei
Class : CSE 472
Organization : ASU CIDSE
Project : SMM Project 1
Task : Friendship Network Analysis

"""

import networkx as nx
import random as rd
import matplotlib.pyplot as plt


def main():
    friendship_network = init_network()

    node_list = list(range(1, 10))

    edge_list = [(rd.randrange(1, 10), rd.randrange(10)) for x in range(1, 20)]
    edge_list = list(dict.fromkeys(edge_list))

    add_nodes(network=friendship_network, node_list=node_list)

    print(friendship_network.nodes())

    add_edges(network=friendship_network, edge_list=edge_list)

    print(friendship_network.edges())

    print(friendship_network)

    visualize_network(network=friendship_network)
    plot_degree_distribution(network=friendship_network)


def init_network():
    init_g = nx.DiGraph(name='Twitter Friendship Network', course='CSE 472')

    return init_g


def add_nodes(network, node_list):

    for node in node_list:
        network.add_node(node, username='John Doe')


def add_edges(network, edge_list):

    for edge in edge_list:
        network.add_edge(edge[0], edge[1], weight=1)


def visualize_network(network):

    nx.draw_networkx(network)

    plt.show()


def plot_degree_distribution(network):

    degrees = [network.degree(i) for i in network.nodes()]

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    plt.hist(degrees)

    plt.show()


if __name__ == '__main__':
    main()