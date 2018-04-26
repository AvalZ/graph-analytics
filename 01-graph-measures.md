# Centrality measures

Understand which are the most important nodes in a graph.

## Degree centrality

Count number of edges in a node.

* **in_degree** -- number of nodes with the highest edges entering a node
* **out_degree** -- number of nodes with the highest edges exiting a node

A node with high in_degree and out_degree has lots of neightbours, but it does not mean it is the most important node in the network.

## Betweenness centrality

How important a node is in the network with regards to the *flow* of information.
You can "see" the information and also decide how and if you pass the information.

This metric is high to compute (you have to compute all shortest path).

## Closeness centrality

A node has "good" friends.

You are close to nodes with a high betweenness.


# Connected components

## Strongly Connected Components (SCC)

Each node within the component can be reached from every other node in the component by *following directed links*.

## Weakly Connected Components (WCC)

Each node can be reached from every other node by following links *in either directions*.

## In-components

A set of nodes from which you can only go **in**.

## Out-components

A set of nodes from which you can only go **out**.

## Giant component

The largest component that encompasses a significant fraction of the graph.

Giant components make the network "alive" (e.g., the Web).

# Clustering

## Strong and weak ties

Strong ties connect *close* nodes.
Weak ties connect *far* nodes.

## Global clustering

* Closed triad (a triangle of nodes)
* Open triad (a triangle of nodes missing an edge)
* Connected pair
* Unconnected

`C = ( (# of triangles) * 3 ) / (# of connected triples of vertices)`

* C = 1 => all components are a cliques (a fully connected graph)
* C = 0 => no closed triads (a tree)

## Local clustering

Define a clustering index for a single vertex.

Captures the density of links between nodes neighboring a vertex.

`Ci = ( 2 Li ) / ( ki ( ki - 1 ) )`

Maximum Ci: (Ki * (Ki - 1) ) / 2

`C = 1/n SUM(Ci)`

Local clustering can be used as indicators of **structural holes** in a network.
Lower values in Ci means more structural holes, but it also means that the vertex is more important than others.


