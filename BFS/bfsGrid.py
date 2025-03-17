from collections import deque

def bfsGrid(grid, start):
    rows , cols = len(grid), len(cols[0])
    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    q = deque([start])
    visited = set([start])

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0<= nr < rows and 0<= nc < cols and (nr,nc) not in visited:
                q.append((nr,nc))
                visited.add((nr,nc))