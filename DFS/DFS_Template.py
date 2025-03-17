# 1. Tree DFS Template - Three Classic Tree Traversal Patterns
def tree_dfs(root):
    if not root:  # Handle empty tree case
        return
    
    # Pre-order traversal (Root -> Left -> Right)
    def preorder(node):
        if not node:  # Base case: hit None/leaf
            return
        # Process root first, then children
        process(node)     # Visit/process current node FIRST
        preorder(node.left)   # Then entire left subtree
        preorder(node.right)  # Finally entire right subtree
        # Use this pattern when you need to:
        # 1. Copy/clone trees
        # 2. Serialize trees
        # 3. Process parent before children
    
    # In-order traversal (Left -> Root -> Right)
    def inorder(node):
        if not node:
            return
        inorder(node.left)    # Process entire left subtree
        process(node)         # Then current node
        inorder(node.right)   # Finally right subtree
        # Use this pattern when you need:
        # 1. BST traversal in sorted order
        # 2. BST validation
        # 3. Find predecessor/successor
    
    # Post-order traversal (Left -> Right -> Root)
    def postorder(node):
        if not node:
            return
        postorder(node.left)  # Process left subtree
        postorder(node.right) # Then right subtree
        process(node)         # Finally current node
        # Use this when you need:
        # 1. Delete trees (process children before parent)
        # 2. Calculate subtree results before parent

# 2. Matrix/Grid DFS Template - For 2D Array Traversal Problems
def grid_dfs(grid):
    if not grid or not grid[0]:  # Handle empty grid cases
        return
    
    rows, cols = len(grid), len(grid[0])
    visited = set()  # Track visited cells to avoid cycles
    
    def dfs(r, c):
        # Four critical checks before processing any cell:
        if (r < 0 or r >= rows or    # 1. Row within bounds
            c < 0 or c >= cols or    # 2. Column within bounds
            (r, c) in visited or     # 3. Not already visited
            not is_valid(grid[r][c])): # 4. Valid cell to visit
            return
        
        visited.add((r, c))  # Mark as visited
        
        # Classic 4-directional movement pattern
        directions = [(1, 0),   # down
                     (-1, 0),  # up
                     (0, 1),   # right
                     (0, -1)]  # left
        for dr, dc in directions:
            dfs(r + dr, c + dc)  # Explore each direction
        # Use this for:
        # 1. Island problems
        # 2. Flood fill
        # 3. Matrix region problems

# 3. Graph DFS Template - For General Graph Traversal
def graph_dfs(graph):
    visited = set()  # Track visited nodes
    
    def dfs(node):
        if node in visited:  # Prevent cycles
            return
        
        visited.add(node)  # Mark current node as visited
        process(node)      # Process current node
        
        # Visit all adjacent nodes/neighbors
        for neighbor in graph[node]:
            dfs(neighbor)  # Recursive call for each neighbor
        # Use this for:
        # 1. Connected components
        # 2. Graph traversal
        # 3. Reachability problems

# 4. Path Finding DFS Template - Finding Paths Between Nodes
def path_finding_dfs(graph, start, target):
    visited = set()
    path = []  # Track current path
    
    def dfs(node):
        if node == target:  # Found the target
            return True
        
        if node in visited:  # Prevent cycles
            return False
        
        visited.add(node)
        path.append(node)  # Add to current path
        
        # Try all possible next steps
        for neighbor in graph[node]:
            if dfs(neighbor):  # If path found
                return True
        
        path.pop()  # Backtrack if no path found
        return False
        # Use this for:
        # 1. Finding specific paths
        # 2. Route finding
        # 3. Maze solving

# 5. Backtracking DFS Template - For Combinatorial Problems
def backtracking_dfs(nums):
    result = []  # Store all valid solutions
    
    def dfs(path, options):
        if is_solution(path):  # Check if current path is a solution
            result.append(path[:])  # Add copy of path to results
            return
        
        # Try each remaining option
        for i, option in enumerate(options):
            # 1. Make a choice
            path.append(option)
            
            # 2. Explore further with that choice
            dfs(path, options[:i] + options[i+1:])
            
            # 3. Undo the choice (backtrack)
            path.pop()
        # Use this for:
        # 1. Permutations
        # 2. Combinations
        # 3. Subset generation
    
    dfs([], nums)
    return result