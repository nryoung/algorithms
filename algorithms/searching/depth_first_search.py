"""
    depth_first_search.py

    Recursive implementation of DFS algorithm on a graph.

    Depth First Search Overview:
    ------------------------
    Used to traverse trees, tree structures or graphs.
    Starts at a selected node (root) and explores the branch
    as far as possible before backtracking.

    Time Complexity: O(E + V)
        E = Number of edges
        V = Number of vertices (nodes)

    Pseudocode: https://en.wikipedia.org/wiki/Depth-first_search
"""


def dfs(graph, start, path=[]):
    if start not in graph or graph[start] is None or graph[start] == []:
        return None
    path = path + [start]
    for edge in graph[start]:
        if edge not in path:
            path = dfs(graph, edge, path)
    return path
