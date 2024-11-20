### Name: Yash Daswani  
### Student ID: `1002257766`  

## Overview  
This repository contains implementations for the following algorithms:  
1. **Depth-First Search (DFS)**  
2. **Kruskal's Algorithm**  
3. **Topological Sort**  

## Algorithms  

### 1. Depth-First Search (DFS)  
- **Graph Representation**: Adjacency list.  
- **Functionality**: Recursively visits nodes and their unvisited neighbors. Tracks visited nodes to prevent revisits.  

### 2. Kruskal's Algorithm  
- **Input**: A weighted graph represented as edges in the form `(u, v, weight)`.  
- **Methodology**:  
  - Sort edges by weight.  
  - Use Union-Find to avoid cycles while adding edges to the Minimum Spanning Tree (MST).  

### 3. Topological Sort  
- **Graph Representation**: Directed graph using an adjacency list.  
- **Methodology**:  
  - Perform DFS for all nodes.  
  - After visiting a node's neighbors, add it to a stack.  
  - Reverse the stack to get the topological order.  
