from collections import defaultdict

graph = {
    'm': ['q', 'r', 'x'],
    'n': ['q', 'u'],
    'o': ['r', 's', 'v'],
    'p': ['o', 's', 'z'],
    'q': ['t'],
    'r': ['u', 'y'],
    's': ['r'],
    't': ['x', 'y'],
    'u': ['t'],
    'v': ['w', 'z'],
    'w': [],
    'x': [],
    'y': ['v'],
    'z': []
}


visited = set()
stack = []


def dfs(node):
    if node not in visited:
        visited.add(node)  
        for neighbor in graph[node]:  
            dfs(neighbor)
        stack.append(node)  

# Topological sort function
def topological_sort(graph):
    for node in graph.keys():
        if node not in visited:
            dfs(node)
    return stack[::-1]  


result = topological_sort(graph)


print("Topological Sort Order:")
print(result)


# OUTPUT

# Topological Sort Order:
# ['p', 'o', 's', 'n', 'm', 'r', 'u', 'q', 't', 'y', 'v', 'z', 'w', 'x']
