from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Updates the grid such that each cell's value represents:
        - The shortest distance to the nearest 0 for reachable cells.
        - -1 remains unchanged for unreachable cells.
        """
        ROWS, COLS = len(grid), len(grid[0])  # Get the dimensions of the grid
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible directions of movement
        q = deque()  # Initialize the queue for BFS

        # Step 1: Add all cells with value 0 to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:  # Find all starting points (0 cells)
                    q.append((r, c))  # Add them to the queue

        # Step 2: Perform BFS to compute the minimum distance
        while q:
            r, c = q.popleft()  # Get the next cell from the queue

            # Explore all 4 neighboring cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc  # Calculate the new row and column
                
                # Check if the neighbor is valid for BFS
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1  # Update the neighbor's distance
                    q.append((nr, nc))  # Add the neighbor to the queue

if __name__ == "__main__":
    # Example usage:
    grid = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]

    print("Original Grid:")
    for row in grid:
        print(row)

    # Create a Solution object and apply the method
    solution = Solution()
    solution.islandsAndTreasure(grid)

    print("\nUpdated Grid:")
    for row in grid:
        print(row)
