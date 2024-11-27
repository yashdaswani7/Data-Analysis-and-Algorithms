import heapq

def dijkstra(graph, source, end=None):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    if end:
        return distances[end] if end in distances else float('infinity')
    
    return distances

# Example Graph for Dijkstra's Algorithm
graph_dijkstra = {
    's': {'t': 10, 'y': 5},
    't': {'x': 1, 'y': 2},
    'y': {'t': 3, 'x': 9, 'z': 2},
    'x': {'z': 4},
    'z': {'s': 7, 'x': 6}
}

source = 's'
end = 'z'
result_dijkstra = dijkstra(graph_dijkstra, source, end)
print(f"Dijkstra's Algorithm Result (from source '{source}' to '{end}'):")
print(result_dijkstra)

# Running Dijkstra's Algorithm for all nodes
result_dijkstra_all = dijkstra(graph_dijkstra, source)
print(f"\nDijkstra's Algorithm Result (from source '{source}' to all nodes):")
print(result_dijkstra_all)


# OUTPUT

# Dijkstra's Algorithm Result (from source 's' to 'z'):
# 7

# Dijkstra's Algorithm Result (from source 's' to all nodes):
# {'s': 0, 't': 8, 'y': 5, 'x': 9, 'z': 7}
