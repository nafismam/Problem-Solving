def dfs_recursive(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        dfs_recursive(graph, neighbor, visited)

# Example Graph and Call
graph = {  # Define a graph as an adjacency list (dictionary where keys are nodes and values are lists of neighbors).
    1: [2, 3],  # Node 1 has neighbors 2 and 3.
    2: [4],     # Node 2 has a neighbor 4.
    3: [],      # Node 3 has no neighbors (an empty list).
    4: []       # Node 4 also has no neighbors.
}
visited = set()  # Initialize an empty set to keep track of visited nodes.
dfs_recursive(graph, 1, visited)