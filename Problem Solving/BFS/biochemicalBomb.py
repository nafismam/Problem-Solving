from collections import deque

def biochemical_bomb_single_case(N, M, grid, bomb_r, bomb_c):
    """
    Determines the time it takes to contaminate all people in the city
    or returns -1 if not all can be contaminated.
    """
    # Directions for movement: Right, Left, Down, Up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize BFS
    queue = deque([(bomb_r, bomb_c, 0)])  # (row, col, time)
    visited = set()
    visited.add((bomb_r, bomb_c))  # Mark the bomb's position as visited
    max_time = 0

    # Perform BFS
    while queue:
        r, c, time = queue.popleft()

        # Update maximum time
        max_time = max(max_time, time)

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds and if the cell has people and hasn't been visited
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and grid[nr][nc] == 1:
                visited.add((nr, nc))
                queue.append((nr, nc, time + 1))

        # Check if all people have been contaminated
            for r in range(N):
                for c in range(M):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        return -1  # Not all people can be contaminated

    return max_time


# Example Input
N = 7  # Number of rows
M = 8  # Number of columns
grid = [
    [0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0]
]
bomb_r = 2  # Row of the bomb
bomb_c = 5  # Column of the bomb

# Run the function and print the result
result = biochemical_bomb_single_case(N, M, grid, bomb_r, bomb_c)
print(result)  # Expected Output: 8
