#Implementation of Bipartite Check using DFS
def is_bipartite_dfs(graph):
    """
    Check if graph is bipartite using DFS.
    graph: adjacency list → {node: [neighbors]}
    Returns True if bipartite, else False
    """
    color = {}

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if neighbor not in color:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for node in graph:
        if node not in color:
            if not dfs(node, 0):
                return False
    return True
graph1 = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

graph2 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print(is_bipartite_dfs(graph1))  # True
print(is_bipartite_dfs(graph2))  # False
