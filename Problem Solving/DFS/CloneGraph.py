from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # A dictionary to keep track of visited nodes and their clones
        visited = {}

        def dfs(current_node):
            if current_node in visited:
                return visited[current_node]

            # Clone the node
            clone = Node(current_node.val)
            visited[current_node] = clone

            # Recursively clone neighbors
            for neighbor in current_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        # Start DFS from the given node
        return dfs(node)

# Example Usage
if __name__ == "__main__":
    # Creating the example graph manually
    # Node 1
    node1 = Node(1)
    # Node 2
    node2 = Node(2)
    # Node 3
    node3 = Node(3)
    
    # Defining neighbors
    node1.neighbors = [node2]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2]

    # Clone the graph
    solution = Solution()
    cloned_graph = solution.cloneGraph(node1)

    # Printing the cloned graph structure
    print("Cloned Node Value:", cloned_graph.val)
    print("Neighbors of Cloned Node 1:", [n.val for n in cloned_graph.neighbors])
    print("Neighbors of Cloned Node 2:", [n.val for n in cloned_graph.neighbors[0].neighbors])
