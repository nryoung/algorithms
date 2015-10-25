"""
    breadth_first_search.py

    Iterative implementation of BFS algorithm on a graph.

    Breadth First Search Overview:
    ------------------------
    Used to traverse trees, tree structures or graphs.
    Starts at a selected node (root) and explores the nearest
    neighbor branches before proceeding further.

    Time Complexity: O(E + V)
        E = Number of edges
        V = Number of vertices (nodes)

    Pseudocode: https://en.wikipedia.org/wiki/Breadth-first_search
"""


def bfs(graph, start):
    if start not in graph or graph[start] is None or graph[start] == []:
        return None
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
