"""
    Disjoint set.
    Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.rank: int
        self.parent: Node


def make_set(x: Node) -> None:
    """
    Make x as a set.
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    x.parent = x


def union_set(x: Node, y: Node) -> None:
    """
    Union of two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = find_set(x), find_set(y)
    if x == y:
        return

    elif x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def find_set(x: Node) -> Node:
    """
    Return the parent of x
    """
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def find_python_set(node: Node) -> set:
    """
    Return a Python Standard Library set that contains i.
    """
    sets = ({0, 1, 2}, {3, 4, 5})
    for s in sets:
        if node.data in s:
            return s
    msg = f"{node.data} is not in {sets}"
    raise ValueError(msg)