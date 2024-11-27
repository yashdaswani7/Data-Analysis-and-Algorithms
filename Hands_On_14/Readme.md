### Name: Yash Daswani  
### Student ID: `1002257766`  

## Overview
This repository contains the implementation of the following algorithms:  
1. **Dijkstra's Algorithm**  
2. **Bellman-Ford Algorithm**  
3. **Floyd-Warshall Algorithm**  

## Algorithms

### 1. Dijkstra's Algorithm
- **Graph Representation**: Uses an adjacency list where nodes map to their neighbors and associated edge weights.  
- **Purpose**: Determines the shortest path from a single source node to all other nodes in a graph with non-negative edge weights.  
- **Key Features**:  
  - Utilizes a priority queue implemented with a min-heap.  
  - Supports finding the shortest distance to a specified target node.  

---

### 2. Bellman-Ford Algorithm
- **Input**: A graph represented as a list of edges in the format `(u, v, weight)`.  
- **Process**:  
  - Iteratively relaxes edges to calculate the shortest paths from a single source node to all other nodes.  
  - Detects the presence of negative-weight cycles.  
- **Output**:  
  - Computes the shortest distances to all nodes or provides a warning if a negative-weight cycle exists.  
  - Includes functionality to reconstruct shortest paths using predecessor nodes.  

---

### 3. Floyd-Warshall Algorithm
- **Graph Representation**: Operates on an adjacency matrix that stores distances between every pair of nodes.  
- **Purpose**: Computes the shortest paths between all pairs of nodes in the graph.  
- **Key Features**:  
  - Dynamically updates the adjacency matrix in-place using a dynamic programming approach.  
  - Supports negative edge weights but does not detect negative-weight cycles.  
