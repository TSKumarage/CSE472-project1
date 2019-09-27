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


def read_data(raw= False, type='numpy'):

    code_dir = os.path.dirname(__file__)  # absolute dir

    rel_path = os.path.join(code_dir, "graph_data", "edge_graph.csv")

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



