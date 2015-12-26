"""
    Depth First Search
    ------------------
    Recursive implementation of the depth first search algorithm used to
    traverse trees or graphs. Starts at a selected node (root) and explores the
    branch as far as possible before backtracking.

    Time Complexity: O(E + V)

        E = Number of edges

        V = Number of vertices (nodes)

    Pseudocode: https://en.wikipedia.org/wiki/Depth-first_search
"""


def dfs(graph, start, path=[]):
    """
    Depth first search that recursively searches the path. Backtracking occurs
    only when the last node in the path is visited.

    :param graph: A dictionary of nodes and edges.
    :param start: The node to start the recursive search with.
    :param path: A list of edges to search.
    :rtype: A boolean indicating whether the node is included in the path.

    """
    if start not in graph or graph[start] is None or graph[start] == []:
        return None
    path = path + [start]
    for edge in graph[start]:
        if edge not in path:
            path = dfs(graph, edge, path)
    return path
