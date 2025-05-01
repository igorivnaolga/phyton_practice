from heapq import heappush, heappop
import networkx as nx

def prim_mst(graph):
    # Create empty MST
    mst = nx.Graph()

    # Start with an arbitrary node
    visited = {list(graph.nodes())[0]}

    # Priority queue of edges
    edges = []
    for u, v, weight in graph.edges(data='weight', nbunch=visited):
        heappush(edges, (weight, u, v))

    # Until all nodes are visited
    while visited != set(graph.nodes()):
        weight, u, v = heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.add_edge(u, v, weight=weight)
            for v2, v3, new_weight in graph.edges(data='weight', nbunch=[v]):
                if v3 not in visited:
                    heappush(edges, (new_weight, v2, v3))

    return mst

# Create demo graph
G = nx.Graph()
G.add_edge('A', 'B', weight=7)
G.add_edge('A', 'D', weight=5)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'D', weight=9)
G.add_edge('B', 'E', weight=7)
G.add_edge('C', 'E', weight=5)
G.add_edge('D', 'E', weight=15)
G.add_edge('D', 'F', weight=6)
G.add_edge('E', 'F', weight=8)
G.add_edge('E', 'G', weight=9)
G.add_edge('F', 'G', weight=11)

# Run Prim's algorithm
mst = prim_mst(G)

# Output MST edges
print("Edges in the MST:")
for edge in mst.edges(data=True):
    print(edge)
