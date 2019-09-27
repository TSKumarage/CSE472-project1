"""
Authors : Kumarage Tharindu & Fan Lei
Class : CSE 472
Organization : ASU CIDSE
Project : SMM Project 1
Task : Friendship Network Analysis

"""

import networkx as nx
import matplotlib.pyplot as plt
import data_extraction.data_reader as dt


def main():
    friendship_network = init_network()

    node_list, edge_list = dt.read_data()

    add_nodes(network=friendship_network, node_list=node_list)

    add_edges(network=friendship_network, edge_list=edge_list)

    print("Network Analysis of: ", friendship_network)
    print()

    basic_network_report(network=friendship_network)  # print a basic analysis report on the network

    plot_degree_distribution(network=friendship_network, plot_type='all')  # plot degree distribution

    clustering_coefficient(network=friendship_network)  # plot and report local clustering coefficient

    network_centrality(network=friendship_network)
    # plot and report network centrality measures (degree, betweenness, closeness)




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

    nx.draw_random(network)

    plt.savefig("graph.png", dpi=1000)


def basic_network_report(network):
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

    if plot_type == 'in' or plot_type =='all':

        in_degree_mat = network.in_degree()
        in_degree_values = sorted([node[1] for node in in_degree_mat])
        in_degrees = sorted(list(set(in_degree_values)))  # Get the unique in_degree values(bins)
        in_degree_freq = [in_degree_values.count(i) for i in in_degrees]

        if plot_type == 'in':
            plt.title("In Degree Distribution")
            plt.grid(True)
            plt.ylabel("Frequency")
            plt.xlabel("Degree")
            plt.plot(in_degrees, in_degree_freq, 'bx-')
            plt.hist(in_degree_values)

            plt.show()

    if plot_type == 'out' or plot_type =='all':
        out_degree_mat = network.out_degree()
        out_degree_values = sorted([node[1] for node in out_degree_mat])
        out_degrees = sorted(list(set(out_degree_values))) # Get the unique in_degree values(bins)
        out_degree_freq = [out_degree_values.count(i) for i in out_degrees]

        if plot_type == 'out':
            plt.title("Out Degree Distribution")
            plt.grid(True)
            plt.ylabel("Frequency")
            plt.xlabel("Degree")

            plt.plot(out_degrees, out_degree_freq, 'ro-')
            plt.hist(out_degree_values)

            plt.show()

    if plot_type == 'all':
        plt.title("Degree Distribution")
        plt.grid(True)
        plt.ylabel("Frequency")
        plt.xlabel("Degree")
        plt.legend(['In degree', 'Out degree'])
        plt.plot(in_degrees, in_degree_freq, 'bx-')
        plt.plot(out_degrees, out_degree_freq, 'ro-')

        plt.show()


def clustering_coefficient(network):

    local_clustering_list = nx.clustering(network)
    local_clustering_values = sorted([local_clustering_list[node] for node in local_clustering_list])

    average_clustering = nx.average_clustering(network)

    print()
    print("{:^65}".format("----------Network Clustering Coefficient----------"))
    print()
    format_string = "{0:>40} : {1:<5.2f}"
    print(format_string.format("Average Clustering Coefficient of the Network", average_clustering))

    plt.title("Local Clustering Coefficient Distribution")
    plt.grid(True)
    plt.ylabel("Frequency")
    plt.xlabel("Local Clustering Coefficient")
    plt.hist(local_clustering_values)

    plt.show()

def network_centrality(network):

    page_rank_list = nx.pagerank(network)
    page_rank_values = sorted([page_rank_list[node] for node in page_rank_list])

    betweenness_list = nx.betweenness_centrality(network)
    betweenness_values = sorted([betweenness_list[node] for node in betweenness_list])

    closeness_list = nx.closeness_centrality(network)
    closeness_values = sorted([closeness_list[node] for node in closeness_list])

    plt.title("Degree Centrality Distribution (Pagerank)")
    plt.grid(True)
    plt.ylabel("Frequency")
    plt.xlabel("Degree Centrality")
    plt.hist(page_rank_values)

    plt.show()

    plt.title("Betweenness Centrality Distribution")
    plt.grid(True)
    plt.ylabel("Frequency")
    plt.xlabel("Betweenness Centrality")
    plt.hist(betweenness_values)

    plt.show()

    plt.title("Closeness Centrality Distribution")
    plt.grid(True)
    plt.ylabel("Frequency")
    plt.xlabel("Closeness Centrality")
    plt.hist(closeness_values)

    plt.show()


if __name__ == '__main__':
    main()