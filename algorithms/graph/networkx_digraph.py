import networkx as nx
import matplotlib.pyplot as plt

DG = nx.DiGraph()

DG.add_edge("A", "B")
DG.add_edge("B", "A")

G = nx.Graph()
G.add_edges_from([("A","B"), ("B", "C")])
DG = nx.DiGraph(G)

DG = nx.DiGraph()
DG.add_edges_from([("A", "B"), ("B", "C")])
G = nx.Graph(DG)

G.add_node(1)
G.add_node("A")
G.add_node((2, 3))

G.add_edge(1, "A", weight=2.5, label="connection")

G.nodes[1]["color"] = "red"
G.edges[1, "A"]["label"] = "bridge"

neighbors_of_A = G["A"] # {'B': {}, 'C': {}}

edge_info = G["A"]["B"]  # {}

edge_weight = G["A"]["B"]["weight"]

G.graph["name"] = "My Graph"

G.nodes["A"]["color"] = "blue"

G["A"]["B"]["weight"] = 5

G.add_node("A", color="red")
G.add_edge("A", "B", weight=4)


# Draw the graph
nx.draw(DG, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)

# Display it
plt.show()