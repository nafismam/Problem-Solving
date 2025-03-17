from collections import deque

def laughing_bomb(T, test_cases):
    results = []

    for t in range(T):
        # Parse each test case
        N, M = test_cases[t]['dimensions']
        grid = test_cases[t]['grid']
        bomb_r, bomb_c = test_cases[t]['bomb']

        # Directions for BFS: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Initialize BFS queue
        queue = deque([(bomb_r, bomb_c, 0)])  # (row, col, time)
        visited = set()
        visited.add((bomb_r, bomb_c))
        max_time = 0  # Track the maximum time for contamination

        # Perform BFS
        while queue:
            r, c, time = queue.popleft()

            # Update maximum time
            max_time = max(max_time, time)

            # Spread contamination
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check bounds and unvisited cells with people
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and grid[nr][nc] == 1:
                    visited.add((nr, nc))
                    grid[nr][nc] == 2
                    queue.append((nr, nc, time + 1))

        # Final check to ensure all reachable people are contaminated
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 2:
                    max_time = -1  # Not all people are reachable
                    break

        results.append(f"Case #{t + 1}")
        results.append(str(max_time))

    return results

# Input Example
T = 2
test_cases = [
    {
        "dimensions": (7, 8),
        "grid": [
            [0, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0]
        ],
        "bomb": (2, 5)
    },
    {
        "dimensions": (10, 10),
        "grid": [
            [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [2, 2, 1, 1, 1, 1, 0, 1, 0, 1]
        ],
        "bomb": (2, 2)
    }
]

# Run the function and print results
results = laughing_bomb(T, test_cases)
for line in results:
    print(line)
