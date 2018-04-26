# Network models

* Simple representation of complex networks
* Can derive properties mathematically
* Predict properties and outcomes

## Erdös-Rényi random graphs

* Start with N isolated nodes and connect them
* Resulting network is undirected
* Key parameters: **p** and **M**
    * p = probability that any pair of nodes share an edge
    * M = total number of edges in the graph

`G(N,p)` or `G(N,M)`

Graph creation is a **democratic process** (equal probability) and it is guided by **mean values**.

Graph evolution starts from **isolated nodes**.

### Degree distribution in random networks

* p -> 0, nodes are mainly isolated
* p -> 1, nodes are mainly connected

Probability that a node has k links: **Binomial distribution**
(can be approximated to Poisson for N>>k

How does the size of the **giant component** vary?
* p = 0, k = 0 (only isolated nodes)
* p = 1, k = N-1 (the network is a complete graph)
* for the emergence of the giant component, we need k = 1 (on average).
    * subcritical: `p <1/n, k < 1`
    * critical: `p = 1/n, k=1`
    * supercritical: `p > 1/n, k > 1`
    * connected: `p > ln n`
