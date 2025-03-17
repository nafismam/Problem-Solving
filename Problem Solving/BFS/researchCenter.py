from collections import deque
from itertools import combinations

def bfs_research_center(N, M, K, R, centers, grid):
    """
    Determines the minimum number of research centers needed to cover all '1' cells in the grid.

    Parameters:
    N (int): Number of rows in the grid.
    M (int): Number of columns in the grid.
    K (int): Maximum number of research centers to consider.
    R (int): Coverage radius of each research center.
    centers (List[Tuple[int, int]]): List of potential research center locations.
    grid (List[List[int]]): 2D grid representing the area.

    Returns:
    int: Minimum number of research centers needed to cover all '1' cells in the grid.
    """
    def check_coverage(center_locations):
        """
        Performs BFS from the given center locations to calculate covered '1' cells.

        Parameters:
        center_locations (List[Tuple[int, int]]): Chosen research center locations.

        Returns:
        int: Number of '1' cells covered by the chosen centers.
        """
        visited = set()  # Track visited cells
        queue = deque()  # Initialize queue for BFS
        covered_ones = set()  # Track covered '1' cells

        # Initialize BFS from all chosen center locations
        for cx, cy in center_locations:
            queue.append((cx, cy, 0))  # Add (row, col, distance) to queue
            visited.add((cx, cy))  # Mark center as visited

        while queue:
            x, y, dist = queue.popleft()

            # Mark cell as covered if it's within radius and contains '1'
            if dist <= R and grid[x][y] == 1:
                covered_ones.add((x, y))

            # Stop exploring this path if the radius is exceeded
            if dist >= R:
                continue

            # Explore all 4 possible directions (up, down, left, right)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy

                # Ensure the new position is within bounds and not visited
                if (0 <= nx < N and 
                    0 <= ny < M and 
                    (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

        return len(covered_ones)

    # Count the total number of '1' cells in the grid
    total_ones = sum(row.count(1) for row in grid)
    print(f"Total cells to cover: {total_ones}")

    # Try each number of centers from 1 to K
    for k in range(1, K + 1):
        # Try all combinations of 'k' centers
        for center_combo in combinations(centers, k):
            covered = check_coverage(center_combo)  # Calculate coverage for this combination
            if covered == total_ones:  # Check if all '1' cells are covered
                print(f"Found solution with {k} centers covering all {total_ones} cells")
                print(f"Center locations used: {center_combo}")
                return k  # Return the number of centers needed

    return K  # Return K if no solution is found with fewer centers


# Example Input
N = 10  # Grid height
M = 10  # Grid width
K = 4   # Maximum number of research centers allowed
R = 3   # Coverage radius of each research center
centers = [(2, 2), (3, 7), (5, 4), (7, 3), (8, 8), (4, 5)]  # Possible research center locations
grid = [
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1]
]

# Solve the problem
result = bfs_research_center(N, M, K, R, centers, grid)
print(f"\nMinimum number of research centers needed: {result}")