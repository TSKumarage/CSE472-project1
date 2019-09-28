"""
Authors : Kumarage Tharindu & Fan Lei
Class : CSE 472
Organization : ASU CIDSE
Project : SMM Project 1
Task : File reader : Provider other package the access to the graph data

"""

import os
import numpy as np
import pandas as pd


def write_data(data, type='numpy'):

    rel_path = get_data_repo_path()
    header = ["Source", "Target"]
    if type == 'pandas':
        data.to_csv(rel_path, header=header, index=False)
    elif type == 'numpy':
        header_str = ""
        for item in header:
            header_str += item+","
        header_str = header_str.rstrip(',')
        np.savetxt(rel_path, data, delimiter=",", header=header_str)


def read_data(raw= False, type='numpy'):

    rel_path = get_data_repo_path()
    data = pd.read_csv(rel_path)

    if raw:
        if type == 'pandas':
            return data
        if type == 'numpy':
            return data.values
    else:
        nodes = list(np.unique(data.iloc[:,1:].values))
        edges = list(data.values)

        return nodes, edges


def get_data_repo_path():
    code_dir = os.path.dirname(__file__)  # absolute dir

    rel_path = os.path.join(code_dir, "graph_data", "edge_graph.csv")

    return rel_path



