def bellman_ford(edge_list, source_node):
    nodes = set()
    for src, dest, cost in edge_list:
        nodes.add(src)
        nodes.add(dest)
    
    min_distances = {node: float('inf') for node in nodes}
    predecessors = {node: None for node in nodes}
    min_distances[source_node] = 0

    for _ in range(len(nodes) - 1):
        for src, dest, cost in edge_list:
            if min_distances[src] + cost < min_distances[dest]:
                min_distances[dest] = min_distances[src] + cost
                predecessors[dest] = src

    for src, dest, cost in edge_list:
        if min_distances[src] + cost < min_distances[dest]:
            return min_distances, predecessors, True  # Negative cycle detected

    return min_distances, predecessors, False

def reconstruct_path(predecessors, source_node, target_node):
    path = []
    current = target_node
    while current is not None:
        path.append(current)
        current = predecessors[current]
    return path[::-1] if path and path[-1] == source_node else []

# Test cases from diagrams
test_cases = [
    {
        "edge_list": [
            ('s', 't', 6), ('s', 'y', 7), 
            ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4), 
            ('y', 't', -3), ('y', 'x', 9), ('y', 'z', 2),
            ('z', 's', 7), ('z', 'x', 6),
            ('x', 'z', -2)
        ],
        "source_node": 's',
        "description": "Graph (a)"
    }
]

print("Bellman-Ford Algorithm Test Cases\n" + "=" * 40)
for i, test_case in enumerate(test_cases, 1):
    edge_list = test_case["edge_list"]
    source_node = test_case["source_node"]
    description = test_case["description"]

    print(f"\nTest Case {i}: {description}")
    print(f"Edges: {edge_list}")
    print(f"Start Node: {source_node}")

    min_distances, predecessors, has_negative_cycle = bellman_ford(edge_list, source_node)

    if has_negative_cycle:
        print("Result: Negative-weight cycle detected.")
    else:
        print(f"Shortest Distances: {min_distances}")
        print(f"Predecessors: {predecessors}")
        for node in min_distances:
            path = reconstruct_path(predecessors, source_node, node)
            print(f"Shortest Path to {node}: {path if path else 'No path exists'}")


# OUTPUT
# Bellman-Ford Algorithm Test Cases
# ========================================

# Test Case 1: Graph (a)
# Edges: [('s', 't', 6), ('s', 'y', 7), ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4), ('y', 't', -3), ('y', 'x', 9), ('y', 'z', 2), ('z', 's', 7), ('z', 'x', 6), ('x', 'z', -2)]
# Start Node: s
# Shortest Distances: {'y': 7, 'x': 6, 's': 0, 'z': 0, 't': 4}
# Predecessors: {'y': 's', 'x': 'z', 's': None, 'z': 't', 't': 'y'}
# Shortest Path to y: ['s', 'y']
# Shortest Path to x: ['s', 'y', 't', 'z', 'x']
# Shortest Path to s: ['s']
# Shortest Path to z: ['s', 'y', 't', 'z']
# Shortest Path to t: ['s', 'y', 't']
