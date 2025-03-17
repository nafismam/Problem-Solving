from collections import deque

def bfs(graph, start, end):
    q = deque([(start,0)])
    visited = set([start])

    while q:
        current, distance = q.popleft()

        if current == end:
            return distance
        
        for neighbors in graph[current]:
            if neighbors not in visited:
                q.append((current, distance+1))
                visited.add(distance)

