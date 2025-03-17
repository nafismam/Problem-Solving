from collections import deque

def multi_source_bfs(grid):
    rows, cols = len(grid), len(grid[0])

    #initially shobar distance -1
    distance = [[-1 for _ in range(cols)] for _ in range(rows)]

    #source gula add to queue and distance 0
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r,c,0))
                distance[r][c] = 0

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while queue: 
        r, c, dist = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0<= nr < rows and 0<= nc < cols and grid[nr][nc] == 0 and distance[nr][nc] == -1:
                distance[nr][nc] = dist + 1
                queue.append((nr, nc, dist+1))
    return distance

# Example grid
grid = [
    [0, 1, 0, 2],
    [0, 0, 1, 0],
    [2, 0, 0, 0],
    [0, 0, 1, 0]
]

# Run the multi-source BFS function
result = multi_source_bfs(grid)

# Print the result grid
print("Shortest distances from sources:")
for row in result:
    print(row)