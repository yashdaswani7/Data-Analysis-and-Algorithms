edges = [
    ('a', 'b', 4), ('a', 'h', 8),
    ('b', 'c', 8), ('b', 'h', 11),
    ('c', 'i', 2), ('c', 'f', 4), ('c', 'd', 7),
    ('d', 'e', 9), ('d', 'f', 14),
    ('e', 'f', 10),
    ('f', 'g', 2),
    ('g', 'h', 1), ('g', 'i', 6),
    ('h', 'i', 7)
]


edges = sorted(edges, key=lambda edge: edge[2])


def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

# Kruskal's Algorithm
def kruskal(edges):
    
    parent = {}
    rank = {}
    mst = []

    
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])

    
    for node in nodes:
        parent[node] = node
        rank[node] = 0

    
    for edge in edges:
        u, v, weight = edge
        if find(parent, u) != find(parent, v):
            mst.append(edge)  
            union(parent, rank, u, v)

    return mst


mst = kruskal(edges)


print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} with weight {weight}")
    
    
# OUTPUT

# Edges in the Minimum Spanning Tree:
# g -- h with weight 1
# c -- i with weight 2
# f -- g with weight 2
# a -- b with weight 4
# c -- f with weight 4
# c -- d with weight 7
# a -- h with weight 8
# d -- e with weight 9
