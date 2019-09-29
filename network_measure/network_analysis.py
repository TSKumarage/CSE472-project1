"""
Authors : Kumarage Tharindu & Fan Lei
Class : CSE 472
Organization : ASU CIDSE
Project : SMM Project 1
Task : Friendship Network Analysis

"""

import networkx as nx
import matplotlib.pyplot as plt
from ..data_extraction import data_wrapper as dt


def main():  # main method to execute all the analysis steps
    friendship_network = init_network()

    node_list, edge_list = dt.read_data()  # read the stored edge_graph_csv in data repository

    add_nodes(network=friendship_network, node_list=node_list)  # populate nodes

    add_edges(network=friendship_network, edge_list=edge_list)  # populate edges

    print("Network Analysis of: ", friendship_network)
    print()

    basic_network_report(network=friendship_network)  # print a basic analysis report on the network

    plot_degree_distribution(network=friendship_network, plot_type='in')  # plot degree distribution
    plot_degree_distribution(network=friendship_network, plot_type='out')

    clustering_coefficient(network=friendship_network)  # plot and report local clustering coefficient

    network_centrality(network=friendship_network)
    # plot and report network centrality measures (degree, betweenness, closeness)


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

    nx.draw_random(network)

    plt.savefig("graph.png", dpi=1000)


def basic_network_report(network):  # Print a basic report on node distribution and structure of the network
    nodes = network.order()
    edges = network.size()

    in_degree_mat = network.in_degree()
    average_in_degree = round(sum([x[1] for x in in_degree_mat])/nodes)
    max_in_degree = max([x[1] for x in in_degree_mat])

    out_degree_mat = network.out_degree()
    average_out_degree = round(sum([x[1] for x in out_degree_mat]) / nodes)
    max_out_degree = max([x[1] for x in out_degree_mat])

    print("{:^65}".format("----------Basic Network Measures----------"))
    print()
    format_string = "{0:>40} : {1:<5}"
    print(format_string.format("Number of Nodes in the Network", nodes))
    print(format_string.format("Number of Edges in the Network", edges))
    print(format_string.format("Average in-degree", average_in_degree))
    print(format_string.format("Maximum in-degree", max_in_degree))
    print(format_string.format("Average out-degree", average_out_degree))
    print(format_string.format("Maximum out-degree", max_out_degree))
    print(format_string.format("Number of strongly connected components", nx.number_strongly_connected_components(network)))
    print(format_string.format("Number of weakly connected components", nx.number_weakly_connected_components(network)))


def plot_degree_distribution(network, plot_type='all'):
    """
      Plot a histogram of the degree distribution
      :param network: NetworkX graph object
      :param plot_type: decides whether to print both in and out degree distributions in the same graph
      """

    if plot_type == 'in' or plot_type =='all':
        in_degree_mat = network.in_degree()
        in_degree_values = sorted([node[1] for node in in_degree_mat])
        in_degrees = sorted(list(set(in_degree_values)))  # Get the unique in_degree values(bins)
        in_degree_freq = [in_degree_values.count(i) for i in in_degree_values]

        if plot_type == 'in':  # Plot in-degree distribution
            print()
            print("{:^65}".format("----------In-Degree Distribution----------"))
            print()

            format_string = "{:>25} " + "|{:<5}" * len(in_degrees)
            print(format_string.format("Degree", *in_degrees))
            print(format_string.format("Frequency (Num. Nodes)", *in_degree_freq))
            plt.title("In Degree Distribution")
            plt.grid(True)
            plt.ylabel("Frequency (Num. Nodes)")
            plt.xlabel("Degree")
            plt.plot(in_degree_values, in_degree_freq, 'rx-')
            plt.hist(in_degree_values)

            plt.show()

    if plot_type == 'out' or plot_type =='all':

        out_degree_mat = network.out_degree()
        out_degree_values = sorted([node[1] for node in out_degree_mat])
        out_degrees = sorted(list(set(out_degree_values))) # Get the unique in_degree values(bins)
        out_degree_freq = [out_degree_values.count(i) for i in out_degrees]

        if plot_type == 'out':  # Plot out-degree distribution
            print()
            print("{:^65}".format("----------Out-Degree Distribution----------"))
            print()

            format_string = "{:>25} " + "|{:<5}" * len(out_degrees)
            print(format_string.format("Degree", *out_degrees))
            print(format_string.format("Frequency (Num. Nodes)", *out_degree_freq))

            plt.title("Out Degree Distribution")
            plt.grid(True)
            plt.ylabel("Frequency")
            plt.xlabel("Degree")

            plt.plot(out_degrees, out_degree_freq, 'rx-')
            plt.hist(out_degree_values)

            plt.show()

    if plot_type == 'all':  # Plot both in and out-degree plots in same graph
        plt.title("Degree Distribution")
        plt.grid(True)
        plt.ylabel("Frequency")
        plt.xlabel("Degree")
        plt.legend(['In degree', 'Out degree'])
        plt.plot(in_degrees, in_degree_freq, 'rx-')
        plt.plot(out_degrees, out_degree_freq, 'go-')

        plt.show()


def clustering_coefficient(network):  # Report the local clustering coefficient of a given network

    local_clustering_list = nx.clustering(network)
    local_clustering_values = sorted([local_clustering_list[node] for node in local_clustering_list])

    local_clustering = sorted(list(set(local_clustering_values)))  # Get the unique values(bins)
    local_clustering_freq = [local_clustering_values.count(i) for i in local_clustering]

    average_clustering = nx.average_clustering(network)  # Get the average clustering coefficient of a given network

    print()
    print("{:^65}".format("----------Network Clustering Coefficient----------"))
    print()
    format_string = "{0:>40} : {1:<5.6f}"
    print(format_string.format("Average Clustering Coefficient of the Network", average_clustering))
    print()

    format_string = "{:>25} " + "|{:<10.7f}" * len(local_clustering)
    print(format_string.format("Clustering Coefficient", *local_clustering))

    format_string = "{:>25} " + "|{:<10}" * len(local_clustering)
    print(format_string.format("Frequency (Num. Nodes)", *local_clustering_freq))

    plt.title("Local Clustering Coefficient Distribution")
    plt.grid(True)
    plt.ylabel("Frequency")
    plt.xlabel("Local Clustering Coefficient")
    plt.hist(local_clustering_values)
    plt.plot(local_clustering, local_clustering_freq, 'rx-')

    plt.show()


def network_centrality(network):  # Report the centrality measures of a given network
    print()
    print("{:^65}".format("----------Network Centrality Measures----------"))
    print()

    # Report the degree centrality measure (Pagerank) of a given network
    page_rank_list = nx.pagerank(network)
    page_rank_values = sorted([round(page_rank_list[node], 6) for node in page_rank_list])
    page_ranks = sorted(list(set(page_rank_values)))  # Get the unique values(bins)
    page_rank_freq = [page_rank_values.count(i) for i in page_ranks]

    format_string = "{:>30} " + "|{:<10.7f}" * len(page_ranks)
    print(format_string.format("Degree centrality (Pagerank)", *page_ranks))

    format_string = "{:>30} " + "|{:<10}" * len(page_ranks)
    print(format_string.format("Frequency (Num. Nodes)", *page_rank_freq))
    print()

    # Report the betweenness centrality measure (Pagerank) of a given network
    betweenness_list = nx.betweenness_centrality(network)
    betweenness_values = sorted([betweenness_list[node] for node in betweenness_list])
    betweenness = sorted(list(set(betweenness_values)))  # Get the unique values(bins)
    betweenness_freq = [betweenness_values.count(i) for i in betweenness]

    format_string = "{:>30} " + "|{:<10.7f}" * len(betweenness)
    print(format_string.format("Betweenness centrality", *betweenness))

    format_string = "{:>30} " + "|{:<10}" * len(betweenness)
    print(format_string.format("Frequency (Num. Nodes)", *betweenness_freq))
    print()

    # Report the closeness centrality measure (Pagerank) of a given network
    closeness_list = nx.closeness_centrality(network)
    closeness_values = sorted([closeness_list[node] for node in closeness_list])
    closeness = sorted(list(set(closeness_values)))  # Get the unique values(bins)
    closeness_freq = [closeness_values.count(i) for i in closeness]

    format_string = "{:>30} " + "|{:<10.7f}" * len(closeness)
    print(format_string.format("Closeness centrality", *closeness))

    format_string = "{:>30} " + "|{:<10}" * len(closeness)
    print(format_string.format("Frequency (Num. Nodes)", *closeness_freq))

    # Plot the centrality distributions
    plt.title("Degree Centrality Distribution (Pagerank)")
    plt.grid(True)
    plt.ylabel("Frequency")
    plt.xlabel("Degree Centrality")
    plt.hist(page_rank_values)
    plt.plot(page_ranks, page_rank_freq, 'rx-')

    plt.show()

    plt.title("Betweenness Centrality Distribution")
    plt.grid(True)
    plt.ylabel("Frequency")
    plt.xlabel("Betweenness Centrality")
    plt.hist(betweenness_values)
    plt.plot(betweenness, betweenness_freq, 'rx-')

    plt.show()

    plt.title("Closeness Centrality Distribution")
    plt.grid(True)
    plt.ylabel("Frequency")
    plt.xlabel("Closeness Centrality")
    plt.hist(closeness_values)
    plt.plot(closeness, closeness_freq, 'rx-')

    plt.show()


if __name__ == '__main__':
    main()