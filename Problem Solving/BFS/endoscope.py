from collections import deque  # Import deque for efficient BFS queue operations

# Define pipe connections
pipe_connections = {
    1: [(0, 1), (0, -1), (1, 0), (-1, 0)],  # Pipe type 1: Connects in all four directions
    2: [(1, 0), (-1, 0)],  # Pipe type 2: Connects vertically (up and down)
    3: [(0, 1), (0, -1)],  # Pipe type 3: Connects horizontally (left and right)
    4: [(-1, 0), (0, 1)],  # Pipe type 4: Connects up and right
    5: [(1, 0), (0, 1)],   # Pipe type 5: Connects down and right
    6: [(1, 0), (0, -1)],  # Pipe type 6: Connects down and left
    7: [(-1, 0), (0, -1)], # Pipe type 7: Connects up and left
}

# Define reverse connections to validate movement
reverse_connections = {
    (0, 1): (0, -1),  # Right requires a Left connection in the next pipe
    (0, -1): (0, 1),  # Left requires a Right connection in the next pipe
    (1, 0): (-1, 0),  # Down requires an Up connection in the next pipe
    (-1, 0): (1, 0),  # Up requires a Down connection in the next pipe
}

def count_reachable_pipes(N, M, R, C, L, grid):
    """
    Calculate the number of reachable pipes starting from position (R, C) within length L.
    
    Parameters:
    N: int - number of rows in the grid
    M: int - number of columns in the grid
    R: int - starting row (0-based index)
    C: int - starting column (0-based index)
    L: int - maximum length the endoscope can traverse
    grid: List[List[int]] - 2D grid representing pipe types
    
    Returns:
    int - count of reachable pipes
    """
    visited = set()  # Track visited cells to prevent revisiting
    queue = deque([(R, C, 1)])  # Initialize BFS queue with (row, col, current_length)
    visited.add((R, C))  # Mark the starting position as visited
    reachable_pipes = 0  # Initialize counter for reachable pipes

    while queue:  # BFS loop runs until the queue is empty
        r, c, length = queue.popleft()  # Get the current position and traversal length

        if length > L:  # Stop if the current length exceeds the maximum allowed length
            continue

        reachable_pipes += 1  # Count the current pipe as reachable

        current_pipe = grid[r][c]  # Get the pipe type at the current position
        for dr, dc in pipe_connections[current_pipe]:  # Check all possible directions for this pipe
            nr, nc = r + dr, c + dc  # Calculate the new position (neighbor row and column)

            # Check if the new position is within grid bounds
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # Check if the new position has already been visited
            if (nr, nc) in visited:
                continue

            # Check if the new position has a valid pipe (pipe type > 0)
            if grid[nr][nc] == 0:
                continue

            # Check if the new pipe connects back to the current pipe
            next_pipe = grid[nr][nc]  # Get the pipe type of the neighboring position
            if reverse_connections[(dr, dc)] not in pipe_connections[next_pipe]:
                continue  # Skip if there is no valid reverse connection

            # Add the new position to the queue for further exploration
            visited.add((nr, nc))  # Mark the new position as visited
            queue.append((nr, nc, length + 1))  # Enqueue the new position with incremented length

    return reachable_pipes  # Return the total number of reachable pipes

# Example Input (Only one test case)
N = 5  # Grid height
M = 6  # Grid width
R = 2  # Start row (0-based indexing)
C = 1  # Start column (0-based indexing)
L = 3  # Maximum length of the endoscope
grid = [
    [0, 0, 5, 3, 6, 0],
    [0, 0, 2, 0, 2, 0],
    [3, 3, 1, 3, 7, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

# Solve for the single test case
result = count_reachable_pipes(N, M, R, C, L, grid)
print(result)  # Expected Output: 5