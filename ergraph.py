import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnp_random_graph(100, 0.01)

print(G.nodes)
print(G.edges)

print(G.number_of_nodes())
print(G.number_of_edges())

nx.draw_random(G, with_labels=True)

plt.show()
