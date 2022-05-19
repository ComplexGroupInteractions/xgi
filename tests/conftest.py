import xgi
import networkx as nx
import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def edgelist1():
    return [[1, 2, 3], [4], [5, 6], [6, 7, 8]]


@pytest.fixture
def edgelist2():
    return [[1, 2], [3, 4], [4, 5, 6]]


@pytest.fixture
def edgelist3():
    return [[1, 2, 3], [3, 4], [4, 5, 6]]


@pytest.fixture
def edgelist4():
    return [[1, 2, 3], [2, 3, 4, 5], [3, 4, 5]]


@pytest.fixture
def edgelist5():
    return [[0, 1, 2, 3], [4], [5, 6], [6, 7, 8]]


@pytest.fixture
def edgelist6():
    return [[0, 1, 2], [1, 2, 3], [2, 3, 4]]


@pytest.fixture
def edgelist7():
    return [[0, 1, 2], [1, 2, 3], [2, 3, 4], [4]]


@pytest.fixture
def edgelist8():
    return [
        [0, 1],
        [0, 1, 2],
        [0, 2, 3],
        [0, 1, 2, 3, 4],
        [2, 4, 5],
        [1, 3, 5],
        [0, 3, 4],
        [1, 6],
        [0, 6],
    ]


@pytest.fixture
def dict5():
    return {0: [0, 1, 2, 3], 1: [4], 2: [5, 6], 3: [6, 7, 8]}


@pytest.fixture
def incidence5():
    I = np.zeros((9, 4))
    I[0, 0] = I[1, 0] = I[2, 0] = I[3, 0] = I[4, 1] = 1
    I[5, 2] = I[6, 2] = I[6, 3] = I[7, 3] = I[8, 3] = 1
    return I


@pytest.fixture
def dataframe5():
    data = [
        [0, 0],
        [1, 0],
        [2, 0],
        [3, 0],
        [4, 1],
        [5, 2],
        [6, 2],
        [6, 3],
        [7, 3],
        [8, 3],
    ]
    return pd.DataFrame(data)


@pytest.fixture
def bipartite_graph1():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4], bipartite=0)
    G.add_nodes_from(["a", "b", "c"], bipartite=1)
    G.add_edges_from([(1, "a"), (1, "b"), (2, "b"), (2, "c"), (3, "c"), (4, "a")])
    return G


@pytest.fixture
def bipartite_graph2():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4], bipartite=0)
    G.add_nodes_from(["a", "b", "c"], bipartite=2)
    G.add_edges_from([(1, "a"), (1, "b"), (2, "b"), (2, "c"), (3, "c"), (4, "a")])
    return G


@pytest.fixture
def bipartite_graph3():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4])
    G.add_nodes_from(["a", "b", "c"])
    G.add_edges_from([(1, "a"), (1, "b"), (2, "b"), (2, "c"), (3, "c"), (4, "a")])
    return G


@pytest.fixture
def bipartite_graph4():
    # this is to test when the bipartite condition is not true
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4], bipartite=0)
    G.add_nodes_from(["a", "b", "c"], bipartite=1)
    G.add_edges_from([(1, "a"), ("a", "b"), (2, "b"), (2, "c"), (3, "c"), (4, "a")])
    return G


@pytest.fixture
def attr1():
    return {"color": "red", "name": "horse"}


@pytest.fixture
def attr2():
    return {"color": "blue", "name": "pony"}


@pytest.fixture
def attr3():
    return {"color": "yellow", "name": "zebra"}


@pytest.fixture
def attr4():
    return {"color": "red", "name": "orangutan", "age": 20}


@pytest.fixture
def attr5():
    return {"color": "blue", "name": "fish", "age": 2}


@pytest.fixture
def hyperwithattrs(edgelist4, attr1, attr2, attr3, attr4, attr5):
    H = xgi.Hypergraph(edgelist4)
    H.add_nodes_from(
        [
            (1, attr1),
            (2, attr2),
            (3, attr3),
            (4, attr4),
            (5, attr5),
        ]
    )
    return H
