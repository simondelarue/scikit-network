#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests for visualization/graphs.py"""

import unittest

import numpy as np
from scipy import sparse

from sknetwork.data.test_graphs import test_graph_disconnect, test_bigraph_disconnect
from sknetwork.data.toy_graphs import karate_club, painters, movie_actor, bow_tie, star_wars
from sknetwork.visualization.graphs import svg_graph, svg_digraph, svg_bigraph


# noinspection DuplicatedCode
class TestVisualization(unittest.TestCase):

    def test_undirected(self):
        graph = karate_club(True)
        adjacency = graph.adjacency
        position = graph.position
        labels = graph.labels
        image = svg_graph(adjacency, position, labels=labels)
        self.assertEqual(image[1:4], 'svg')
        image = svg_graph(adjacency, position, display_edges=False)
        self.assertEqual(image[1:4], 'svg')
        image = svg_graph(adjacency, position, height=None)
        self.assertEqual(image[1:4], 'svg')
        n = adjacency.shape[0]
        edge_labels = [(0, 1, 0), (1, 1, 1), (3, 10, 2)]
        image = svg_graph(adjacency, position=None, names=np.arange(n), labels=np.arange(n), scores=np.arange(n),
                          seeds=[0, 1], width=200, height=200, margin=10, margin_text=5, scale=3,
                          node_order=np.flip(np.arange(n)),
                          node_size=5, node_size_min=2, node_size_max=6, display_node_weight=True,
                          node_weights=np.arange(n),
                          node_width=2, node_width_max=5, node_color='red', edge_width=2, edge_width_min=2,
                          edge_width_max=4, edge_color='blue', edge_labels=edge_labels, display_edge_weight=True,
                          font_size=14)
        self.assertEqual(image[1:4], 'svg')
        image = svg_graph(adjacency, position=None, labels={0: 0})
        self.assertEqual(image[1:4], 'svg')
        image = svg_graph(adjacency, position=None, scores={0: 0})
        self.assertEqual(image[1:4], 'svg')
        image = svg_graph(adjacency=None, position=position)
        self.assertEqual(image[1:4], 'svg')
        image = svg_graph(adjacency=None, position=position, edge_labels=edge_labels)
        self.assertEqual(image[1:4], 'svg')
        image = svg_graph(adjacency, position, labels, label_colors={0: "red", 1: "blue"})
        self.assertEqual(image[1:4], 'svg')
        image = svg_graph(adjacency, position, labels, label_colors=["red", "blue"])
        self.assertEqual(image[1:4], 'svg')

    def test_directed(self):
        graph = painters(True)
        adjacency = graph.adjacency
        position = graph.position
        names = graph.names
        image = svg_digraph(adjacency, position, names=names)
        self.assertEqual(image[1:4], 'svg')
        image = svg_graph(adjacency, position, display_edges=False)
        self.assertEqual(image[1:4], 'svg')
        n = adjacency.shape[0]
        image = svg_digraph(adjacency, position=None, names=np.arange(n), labels=np.arange(n), scores=np.arange(n),
                            name_position='below', seeds=[0, 1], width=200, height=200, margin=10, margin_text=5,
                            scale=3, node_order=np.flip(np.arange(n)),
                            node_size=5, node_size_min=2, node_size_max=6, display_node_weight=True,
                            node_weights=np.arange(n),
                            node_width=2, node_width_max=5, node_color='red', edge_width=2, edge_width_min=2,
                            edge_width_max=4, edge_color='blue', display_edge_weight=True, font_size=14)
        self.assertEqual(image[1:4], 'svg')
        image = svg_digraph(adjacency, position=None, names=np.arange(n), labels={0: 1, 1: 2}, scores=np.arange(n),
                            seeds=[0, 1], width=200, height=200, margin=10, margin_text=5, scale=3,
                            node_order=np.flip(np.arange(n)), node_size=5, node_size_min=2, node_size_max=6,
                            display_node_weight=True, node_weights=np.arange(n), node_width=2, node_width_max=5,
                            node_color='red', edge_width=2, edge_width_min=2, edge_width_max=4, edge_color='blue',
                            display_edge_weight=True, font_size=14)
        self.assertEqual(image[1:4], 'svg')

    def test_bipartite(self):
        graph = movie_actor(True)
        biadjacency = graph.biadjacency
        names_row = graph.names_row
        names_col = graph.names_col
        image = svg_bigraph(biadjacency, names_row, names_col)
        self.assertEqual(image[1:4], 'svg')
        image = svg_bigraph(biadjacency, display_edges=False)
        self.assertEqual(image[1:4], 'svg')
        image = svg_bigraph(biadjacency, reorder=False)
        self.assertEqual(image[1:4], 'svg')
        n_row, n_col = biadjacency.shape
        position_row = np.random.random((n_row, 2))
        position_col = np.random.random((n_col, 2))
        edge_labels = [(0, 1, 0), (1, 1, 1), (3, 10, 2)]
        image = svg_bigraph(biadjacency=biadjacency, names_row=np.arange(n_row), names_col=np.arange(n_col),
                            labels_row=np.arange(n_row), labels_col=np.arange(n_col), scores_row=np.arange(n_row),
                            scores_col=np.arange(n_col), seeds_row=[0, 1], seeds_col=[1, 2],
                            position_row=position_row, position_col=position_col, color_row='red', color_col='white',
                            width=200, height=200, margin=10, margin_text=5, scale=3, node_size=5,
                            node_size_min=1, node_size_max=30, node_weights_row=np.arange(n_row),
                            node_weights_col=np.arange(n_col), display_node_weight=True, node_width=2, node_width_max=5,
                            edge_labels=edge_labels, edge_width=2, edge_width_min=0.3, edge_width_max=4,
                            edge_color='red', display_edge_weight=True, font_size=14)
        self.assertEqual(image[1:4], 'svg')

    def test_disconnect(self):
        adjacency = test_graph_disconnect()
        position = np.random.random((adjacency.shape[0], 2))
        image = svg_graph(adjacency, position)
        self.assertEqual(image[1:4], 'svg')
        biadjacency = test_bigraph_disconnect()
        image = svg_bigraph(biadjacency)
        self.assertEqual(image[1:4], 'svg')

    def test_membership(self):
        adjacency = bow_tie()
        membership = sparse.csr_matrix([[.5, .5], [0, 0], [1, 0], [0, 1], [0, 1]])
        image = svg_graph(adjacency, membership=membership)
        self.assertEqual(image[1:4], 'svg')
        biadjacency = star_wars()
        membership_row = sparse.csr_matrix([[.5, .5], [0, 0], [1, 0], [0, 1]])
        membership_col = sparse.csr_matrix([[.5, .5], [0, 0], [1, 0]])
        image = svg_bigraph(biadjacency, membership_row=membership_row, membership_col=membership_col)
        self.assertEqual(image[1:4], 'svg')

    def test_labels(self):
        adjacency = bow_tie()
        names = ["aa", "bb", "<>", "a&b", ""]
        image = svg_graph(adjacency, names=names)
        self.assertEqual(image[1:4], 'svg')
