from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = set([start])

    while q:
        current = q.popleft()
        print(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)