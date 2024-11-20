# Graph represented as an adjacency list
graph = {
    's': ['z'],
    'z': ['y', 'w'],
    'y': ['x'],
    'x': ['y'],
    'w': ['x', 'v'],
    'v': ['t', 'u'],
    't': ['v'],
    'u': ['t']
}

# Depth-First Search (DFS) function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited and print it
    visited.add(start)
    print(start, end=" ")
    
    # Visit all the neighbors recursively
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Starting DFS from node 's'
print("DFS Traversal starting from node 's':")
dfs(graph, 's')


# OUTPUT

# DFS Traversal starting from node 's':
# s z y x w v t u
