from typing import List

class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        # Define a helper function to perform DFS starting from cell (r, c)
        def dfs(r, c):
            # Base case: Stop if the cell is out of bounds or is water (0)
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return

            # Mark the current cell as visited by setting it to 0 (turning land into water)
            grid[r][c] = 0

            # Define the four possible directions (up, down, left, right) for exploration
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                # Recursively apply DFS to the neighboring cells
                dfs(r + dr, c + dc)

        # If the grid is empty or improperly structured, return 0 islands
        if not grid or not grid[0]:
            return 0

        # Initialize the count of islands
        num_islands = 0

        # Loop through every cell in the grid
        for r in range(len(grid)):  # Iterate over rows
            for c in range(len(grid[0])):  # Iterate over columns
                # If the current cell is land (1), it's the start of a new island
                if grid[r][c] == 1:
                    num_islands += 1  # Increment the island count
                    dfs(r, c)  # Perform DFS to mark the entire island as visited

        # Return the total number of islands found
        return num_islands

# Example usage
grid = [
    ["1", "1", "0", "0", "1"],  # Input grid as strings
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

# Convert the grid from strings to integers
# This is necessary because the solution assumes grid elements are integers (0 or 1)
grid = [[int(cell) for cell in row] for row in grid]

solution = Solution()
print(solution.numIslands(grid))  # Expected output: 4
