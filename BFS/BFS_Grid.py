from collections import deque

def bfs_in_grid(grid, start, target):
    #row toh 1 each but each row er bhitor 4 ta column tai [0]
    rows, cols = len(grid), len(grid[0])

    #            right    down   left       up
    directions = [(0,1), (1,0), (0, -1), (-1,0)]

    queue = deque([(start[0], start[1], 0)])
    visited = set([start])

    while queue:
        r, c, distance = queue.popleft()

        if (r,c) == target:
            return distance
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0<= nr < rows and 0<= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr,nc,distance+1))
                visited.add((nr, nc))

    return -1
# Example grid
grid = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]
# 0 = open cell, 1 = obstacle

# Define start and target positions
start = (0, 0)  # Top-left corner
target = (3, 3)  # Bottom-right corner

# Run the BFS function
shortest_distance = bfs_in_grid(grid, start, target)
print(f"The shortest path from {start} to {target} is: {shortest_distance}")