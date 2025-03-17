from collections import deque
#python library use korsi for faster enqueue and dequeue

def bfs(graph, start):
    #start is the first node
    queue = deque([start]) #queue initialized
    visited = set([start]) #first node set visited

    while queue:
        current = queue.popleft() #leftmost node popped
        print(current, end=' ')

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],  # Node 'A' is connected to nodes 'B' and 'C'
    'B': ['A', 'D', 'E'],  # Node 'B' is connected to 'A', 'D', and 'E'
    'C': ['A', 'F'],  # Node 'C' is connected to 'A' and 'F'
    'D': ['B'],  # Node 'D' is connected to 'B'
    'E': ['B', 'F'],  # Node 'E' is connected to 'B' and 'F'
    'F': ['C', 'E']  # Node 'F' is connected to 'C' and 'E'
}

# Run BFS starting from node 'A'
bfs(graph, 'A')  # Output will be: A B C D E F