"""
CMSC 501 Fall 2020

Super Graph Coloring
"""
import sys
import random

# Increase the recursion limit to slightly above 1000
sys.setrecursionlimit(1500)


class Node:
    def __init__(self, id, color=0):
        self.id = id
        self.color = color

    def __str__(self):
        return f"Node {self.id} - Color {self.color}"


class Edge:
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2


class Graph:
    def __init__(self, nodes, edges, original_num_colors=0):
        self.nodes = nodes
        self.edges = edges
        self.original_num_colors = original_num_colors
        self.min_number_of_colors = original_num_colors

    def get_random_node(self):
        return random.choice(self.nodes)

    def get_adjacent_nodes(self, node):
        return self.edges[node.id]
        # return [edge.node_2 for edge in edges if edge.node_1.id == node.id]

    def is_color_safe(self, node, adjacent_nodes):
        for other in adjacent_nodes:
            if other.color == node.color:
                return False
        return True


NUM_NODES = None
NUM_EDGES = None

# Read in number of nodes and edges in the graph
line = input()
NUM_NODES, NUM_EDGES = [int(x) for x in line.strip().split(" ")]

# Create the nodes in each graph
nodes = {}
edges = {}
for i in range(NUM_NODES):
    nodes[str(i + 1)] = Node(str(i + 1))
    edges[str(i + 1)] = []

# Read in (u,v) for each (u,v) in the list of edges
for i in range(NUM_EDGES):
    line = input()
    line = line.strip()
    id_1, id_2 = line.split(" ")
    edges[id_1].append(nodes[id_2])
    edges[id_2].append(nodes[id_1])

# Read in the starting color assignments for all nodes
line = input()
starting_colors = [int(x) for x in line.strip().split(" ")]
for i in range(len(nodes)):
    nodes[str(i + 1)].color = starting_colors[i]

G = Graph(
    nodes=list(nodes.values()),
    edges=edges,
    original_num_colors=len(set([c for c in starting_colors if c != 0])),
)


def backtrack_graph_coloring(G, index):
    # Return if all nodes have been visited
    if index == len(G.nodes):
        return True

    for i in range(1, len(G.nodes) + 1):
        G.nodes[index].color = i

        # Is this assignment safe?
        if G.is_color_safe(G.nodes[index], G.get_adjacent_nodes(G.nodes[index])):
            if backtrack_graph_coloring(G, index + 1):
                if i > G.min_number_of_colors:
                    G.min_number_of_colors = i
                return True
            # Next vertex was not colorable with current assignment, reset assignment and try next color
            G.nodes[index].color = 0

    return False


backtrack_graph_coloring(G, 0)
print(G.min_number_of_colors - G.original_num_colors)
for node in G.nodes:
    print(node.color, end=" ")
