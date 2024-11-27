def floyd_warshall(adjacency_matrix):
    nodes = list(adjacency_matrix.keys())
    distance_matrix = {source: {target: adjacency_matrix[source][target] for target in nodes} for source in nodes}

    for intermediate_node in nodes:
        for source_node in nodes:
            for target_node in nodes:
                if distance_matrix[source_node][target_node] > distance_matrix[source_node][intermediate_node] + distance_matrix[intermediate_node][target_node]:
                    distance_matrix[source_node][target_node] = distance_matrix[source_node][intermediate_node] + distance_matrix[intermediate_node][target_node]

    return distance_matrix

def print_matrix(matrix):
    all_nodes = list(matrix.keys())
    print("   ", " ".join(f"{node}" for node in all_nodes))
    for row_node in all_nodes:
        row = [f"{matrix[row_node][col_node]:3}" if matrix[row_node][col_node] != float('inf') else "inf" for col_node in all_nodes]
        print(f"{row_node}: ", " ".join(row))

# Example adjacency matrix
infinity = float('inf')
graph = {
    1: {1: 0, 2: infinity, 3: infinity, 4: infinity},
    2: {1: infinity, 2: 0, 3: 1, 4: 1},
    3: {1: infinity, 2: 1, 3: 0, 4: infinity},
    4: {1: 1, 2: infinity, 3: infinity, 4: 0},
}

print("Initial Adjacency Matrix:")
print_matrix(graph)

# Run Floyd-Warshall and print the results
shortest_paths = floyd_warshall(graph)

print("\nShortest Path Matrix after Floyd-Warshall:")
print_matrix(shortest_paths)


# OUTPUT

# Initial Adjacency Matrix:
#       1 2 3 4
# 1:    0 inf inf inf
# 2:  inf   0   1   1
# 3:  inf   1   0 inf
# 4:    1 inf inf   0

# Shortest Path Matrix after Floyd-Warshall:
#       1 2 3 4
# 1:    0 inf inf inf
# 2:    2   0   1   1
# 3:    3   1   0   2
# 4:    1 inf inf   0
