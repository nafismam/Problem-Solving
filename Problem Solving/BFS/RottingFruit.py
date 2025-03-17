from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])  # Get grid dimensions
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Possible directions of movement

        q = deque()  # Queue for BFS
        fresh = 0  # Count of fresh oranges
        time = 0  # Time counter

        # Initialize the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # Rotten orange
                    q.append((r, c))  # Add to queue
                if grid[r][c] == 1:  # Fresh orange
                    fresh += 1

        # Perform BFS
        while q and fresh > 0:
            for _ in range(len(q)):  # Process all oranges in the current time step
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # If the neighbor is a fresh orange, rot it
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark as rotten
                        q.append((nr, nc))  # Add to queue
                        fresh -= 1  # Decrease fresh count
            time += 1  # Increment time

        # If all fresh oranges are rotten, return the time; otherwise, return -1
        return time if fresh == 0 else -1


if __name__ == "__main__":
    # Example 1
    grid1 = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
    print("Input Grid:")
    for row in grid1:
        print(row)
    result1 = Solution().orangesRotting(grid1)
    print("Output:", result1)
    print()

    # Example 2
    grid2 = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
    print("Input Grid:")
    for row in grid2:
        print(row)
    result2 = Solution().orangesRotting(grid2)
    print("Output:", result2)