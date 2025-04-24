def check_edge(adjacency_matrix, node1, node2):
    if adjacency_matrix[node1][node2] != 0:
        return 1
    else:
        return -1
    

matrix = [
    [0,1,0],
    [1,0,1],
    [0,1,0]
]

print(check_edge(matrix, 0, 1))
print(check_edge(matrix, 0, 2))