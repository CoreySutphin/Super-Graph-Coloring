# CMSC 501 Final Project - Super Graph Coloring

This problem tackles the problem of coloring a graph such that for each edge `(u,v)` in the graph `u` and `v` do not have the same color. Furthermore this program should return the minimum number of colors needed to color the graph in addition to the initial colors supplied.

## Usage

The main program requires no dependencies, however the helper script to generate the input requires the `python-igraph` dependency.

To run the program with a manually entered graph, simply run `python super-graph-coloring.py` and enter the graph into STDIN in the following format:

```
3 2
1 2
1 3
1 0 0
```

where the first line is the number nodes followed by the number of edges. The corresponding `num_edges` lines denote the `(u, v)` edges in the graph.
The final line contains the initial coloring configuration for the nodes in the graph.

Alternatively you can utilize the `generate_graph` helper script to generate a random graph and pipe it into this program in the proper format. Every node will be initialized as uncolored To use:
```
python generate_graph.py num_nodes | python super-graph-coloring.py
```