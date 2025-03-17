def dfs_grid(grid,r, c, visited):
    rows, cols = len(grid), len(grid[0])

    if r<0 or r>= rows or c<0 or c>= cols or grid[r][c] == 0 or (r,c) in visited:
        return

    visited.add((r,c))
    print(f"Visiting: ({r}, {c})")

    dfs_grid(grid, r+1, c, visited)
    dfs_grid(grid, r-1, c, visited)
    dfs_grid(grid, r, c+1, visited)
    dfs_grid(grid, r, c-1, visited)

# Example Grid and Call
grid = [  # Define a 2D grid where 1 represents land and 0 represents water.
    [1, 1, 0],  # Row 0
    [1, 0, 0],  # Row 1
    [0, 0, 1]   # Row 2
]
visited = set()  # Initialize an empty set to keep track of visited cells.
dfs_grid(grid, 0, 0, visited)  # Start DFS from cell (0, 0).