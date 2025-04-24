import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")

G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")

G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

G.remove_node("A")

G.remove_nodes_from(["B", "C"])

G.remove_edge("A", "B")

G.remove_edges_from([("A", "C"), ("B", "D")])

print(G.edges())
print(list(G.neighbors("D")))


# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)

# Display it
plt.show()