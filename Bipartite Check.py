#Implementation of Bipartite Check using DFS
def is_bipartite_dfs(graph):
    """
    Check if an undirected graph is bipartite using DFS.
    
    A bipartite graph can be colored using two colors such that
    no two adjacent vertices have the same color.
    
    Args:
        graph: Adjacency list representation {node: [neighbors]}
    
    Returns:
        True if the graph is bipartite, False otherwise
    
    Example:
        >>> graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
        >>> is_bipartite_dfs(graph)
        True
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
