#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:53:09 2023

@author: Bing.Han
"""

import igraph as ig
import matplotlib.pyplot as plt
import os

def plot_net():

    # # Set up workspace
    # path="igraph"
    # os.chdir(path)

    # Read data
    # g= ig.load("netdata/adjnoun/adjnoun.gml")
    # g= ig.load("netdata/celegansneural/celegansneural.gml")
    # g= ig.load("netdata/football/football.gml")
    # g= ig.load("netdata/lesmis/lesmis.gml")
    g= ig.load("netdata/polbooks/polbooks.gml")
    print(g)

    # Community partitioning
    communities =g.community_edge_betweenness()
    communities =communities.as_clustering()

    # View community partitioning results
    for i, community in enumerate(communities):
        print(f"Community {i}:")
        for v in community:
            print(f"\t{g.vs[v]['label']}")

    # Community color Settings
    num_communities =len(communities)
    palette1= ig.RainbowPalette(n=num_communities)
    for i, community in enumerate(communities):
        g.vs[community]["color"]= i
        community_edges =g.es.select(_within=community)
        community_edges["color"]=i
    g.vs["label"]=["\n\n" + label for label in g.vs["label"]]

    # Visualization
    layout = g.layout("kk")
    fig1, ax1 = plt.subplots()
    ig.plot(
        communities,
        layout = layout,
        target = ax1,
        mark_groups = True,
        palette = palette1,
        vertex_size = 20,
        edge_width = 1.0,
        vertex_label_size = 10
    )
    fig1.set_size_inches(4,4)
    plt.show()
