# https://en.wikipedia.org/wiki/Lowest_common_ancestor
# https://en.wikipedia.org/wiki/Breadth-first_search

from __future__ import annotations

from queue import Queue


def swap(a: int, b: int) -> tuple[int, int]:
    """
    Return a tuple (b, a) when given two integers a and b
    >>> swap(2,3)
    (3, 2)
    >>> swap(3,4)
    (4, 3)
    >>> swap(67, 12)
    (12, 67)
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b


def create_sparse(max_node: int, parent: list[list[int]]) -> list[list[int]]:
    """
    creating sparse table which saves each nodes 2^i-th parent
    """
    j = 1
    while (1 << j) < max_node:
        for i in range(1, max_node + 1):
            parent[j][i] = parent[j - 1][parent[j - 1][i]]
        j += 1
    return parent


# returns lca of node u,v
def lowest_common_ancestor(
    u: int, v: int, level: list[int], parent: list[list[int]]
) -> int:
    # u must be deeper in the tree than v
    if level[u] < level[v]:
        u, v = swap(u, v)
    # making depth of u same as depth of v
    for i in range(18, -1, -1):
        if level[u] - (1 << i) >= level[v]:
            u = parent[i][u]
    # at the same depth if u==v that mean lca is found
    if u == v:
        return u
    # moving both nodes upwards till lca in found
    for i in range(18, -1, -1):
        if parent[i][u] not in [0, parent[i][v]]:
            u, v = parent[i][u], parent[i][v]
    # returning longest common ancestor of u,v
    return parent[0][u]


# runs a breadth first search from root node of the tree
def breadth_first_search(
    level: list[int],
    parent: list[list[int]],
    max_node: int,
    graph: dict[int, list[int]],
    root: int = 1,
) -> tuple[list[int], list[list[int]]]:
    """
    sets every nodes direct parent
    parent of root node is set to 0
    calculates depth of each node from root node
    """
    level[root] = 0
    q: Queue[int] = Queue(maxsize=max_node)
    q.put(root)
    while q.qsize() != 0:
        u = q.get()
        for v in graph[u]:
            if level[v] == -1:
                level[v] = level[u] + 1
                q.put(v)
                parent[0][v] = u
    return level, parent