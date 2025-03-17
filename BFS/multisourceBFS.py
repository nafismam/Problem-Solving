from collections import deque


def multiSourceBfs(grid, source):
    rows, cols = len(grid), len(grid[0])
    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    q = deque([(x, y, 0) for x, y in source])
    visited = set(source)

    while q:
        r, c, distance = q.popleft()

        for dr, dc in directions:
            nr,nc = r+dr, c+dc

            if 0<= nr < rows and 0<= nc < cols and (r,c) not in visited:
                q. append((r,c,distance+1))
                visited.add((r,c))

