"""
Given the number of nodes and edges, generated a graph with random edges.

Will also provide a random initial coloring of the nodes up to M colors. Pass
in M as 0 to set all nodes as uncolored.

Usage:
python generate_graph.py num_nodes num_edges num_colors
"""
import sys
from igraph import Graph

num_nodes = int(sys.argv[1])

graph = Graph.GRG(num_nodes, 0.5)

# Print the resulting graph to stdout
print(num_nodes, len(graph.get_edgelist()))
for edge in graph.get_edgelist():
    print(f"{edge[0] + 1} {edge[1] + 1}")

for i in range(num_nodes):
    print(0, end=" ")
