from collections import deque

def bfs_shortest_path(graph, start, target):
    
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, distance = queue.popleft()

        if current == target:
            return distance
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, distance+1))
                visited.add(neighbor)
    return -1


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],  # Node 'A' is connected to nodes 'B' and 'C'
    'B': ['A', 'D', 'E'],  # Node 'B' is connected to 'A', 'D', and 'E'
    'C': ['A', 'F'],  # Node 'C' is connected to 'A' and 'F'
    'D': ['B'],  # Node 'D' is connected to 'B'
    'E': ['B', 'F'],  # Node 'E' is connected to 'B' and 'F'
    'F': ['C', 'E']  # Node 'F' is connected to 'C' and 'E'
}

# Example usage of the BFS shortest path function
start_node = 'A'
target_node = 'F'

# Call the function and print the result
shortest_distance = bfs_shortest_path(graph, start_node, target_node)
print(f"The shortest path from {start_node} to {target_node} is: {shortest_distance}")