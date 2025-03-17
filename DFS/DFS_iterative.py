def dfs_iterative(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbors in graph[node]:
                stack.append(neighbors)

# Example Graph and Call
graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}
dfs_iterative(graph, 1)