from __future__ import annotations


class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


def display(tree: Node | None) -> None:  # In Order traversal of the tree
    """
    >>> root = Node(1)
    >>> root.left = Node(0)
    >>> root.right = Node(2)
    >>> display(root)
    0
    1
    2
    >>> display(root.right)
    2
    """
    if tree:
        display(tree.left)
        print(tree.data)
        display(tree.right)


def depth_of_tree(tree: Node | None) -> int:
    """
    Recursive function that returns the depth of a binary tree.

    >>> root = Node(0)
    >>> depth_of_tree(root)
    1
    >>> root.left = Node(0)
    >>> depth_of_tree(root)
    2
    >>> root.right = Node(0)
    >>> depth_of_tree(root)
    2
    >>> root.left.right = Node(0)
    >>> depth_of_tree(root)
    3
    >>> depth_of_tree(root.left)
    2
    """
    return 1 + max(depth_of_tree(tree.left), depth_of_tree(tree.right)) if tree else 0


def is_full_binary_tree(tree: Node) -> bool:
    """
    Returns True if this is a full binary tree

    >>> root = Node(0)
    >>> is_full_binary_tree(root)
    True
    >>> root.left = Node(0)
    >>> is_full_binary_tree(root)
    False
    >>> root.right = Node(0)
    >>> is_full_binary_tree(root)
    True
    >>> root.left.left = Node(0)
    >>> is_full_binary_tree(root)
    False
    >>> root.right.right = Node(0)
    >>> is_full_binary_tree(root)
    False
    """
    if not tree:
        return True
    if tree.left and tree.right:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        return not tree.left and not tree.right


"""
Problem Description:
Given a binary tree, return its mirror.
"""


def binary_tree_mirror_dict(binary_tree_mirror_dictionary: dict, root: int):
    if not root or root not in binary_tree_mirror_dictionary:
        return
    left_child, right_child = binary_tree_mirror_dictionary[root][:2]
    binary_tree_mirror_dictionary[root] = [right_child, left_child]
    binary_tree_mirror_dict(binary_tree_mirror_dictionary, left_child)
    binary_tree_mirror_dict(binary_tree_mirror_dictionary, right_child)


def binary_tree_mirror(binary_tree: dict, root: int = 1) -> dict:
    """
    >>> binary_tree_mirror({ 1: [2,3], 2: [4,5], 3: [6,7], 7: [8,9]}, 1)
    {1: [3, 2], 2: [5, 4], 3: [7, 6], 7: [9, 8]}
    >>> binary_tree_mirror({ 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11]}, 1)
    {1: [3, 2], 2: [5, 4], 3: [7, 6], 4: [11, 10]}
    >>> binary_tree_mirror({ 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11]}, 5)
    Traceback (most recent call last):
        ...
    ValueError: root 5 is not present in the binary_tree
    >>> binary_tree_mirror({}, 5)
    Traceback (most recent call last):
        ...
    ValueError: binary tree cannot be empty
    """
    if not binary_tree:
        raise ValueError("binary tree cannot be empty")
    if root not in binary_tree:
        msg = f"root {root} is not present in the binary_tree"
        raise ValueError(msg)
    binary_tree_mirror_dictionary = dict(binary_tree)
    binary_tree_mirror_dict(binary_tree_mirror_dictionary, root)
    return binary_tree_mirror_dictionary


"""
Sum of all nodes in a binary tree.

Python implementation:
    O(n) time complexity - Recurses through :meth:`depth_first_search`
                            with each element.
    O(n) space complexity - At any point in time maximum number of stack
                            frames that could be in memory is `n`
"""


from collections.abc import Iterator


class BinaryTreeNodeSum:
    r"""
    The below tree looks like this
        10
       /  \
      5   -3
     /    / \
    12   8  0

    >>> tree = Node(10)
    >>> sum(BinaryTreeNodeSum(tree))
    10

    >>> tree.left = Node(5)
    >>> sum(BinaryTreeNodeSum(tree))
    15

    >>> tree.right = Node(-3)
    >>> sum(BinaryTreeNodeSum(tree))
    12

    >>> tree.left.left = Node(12)
    >>> sum(BinaryTreeNodeSum(tree))
    24

    >>> tree.right.left = Node(8)
    >>> tree.right.right = Node(0)
    >>> sum(BinaryTreeNodeSum(tree))
    32
    """

    def __init__(self, tree: Node) -> None:
        self.tree = tree

    def depth_first_search(self, node: Node | None) -> int:
        if node is None:
            return 0
        return node.value + (
            self.depth_first_search(node.left) + self.depth_first_search(node.right)
        )

    def __iter__(self) -> Iterator[int]:
        yield self.depth_first_search(self.tree)



class BinaryTreePathSum:
    r"""
    The below tree looks like this
          10
         /  \
        5   -3
       / \    \
      3   2    11
     / \   \
    3  -2   1


    >>> tree = Node(10)
    >>> tree.left = Node(5)
    >>> tree.right = Node(-3)
    >>> tree.left.left = Node(3)
    >>> tree.left.right = Node(2)
    >>> tree.right.right = Node(11)
    >>> tree.left.left.left = Node(3)
    >>> tree.left.left.right = Node(-2)
    >>> tree.left.right.right = Node(1)

    >>> BinaryTreePathSum().path_sum(tree, 8)
    3
    >>> BinaryTreePathSum().path_sum(tree, 7)
    2
    >>> tree.right.right = Node(10)
    >>> BinaryTreePathSum().path_sum(tree, 8)
    2
    """

    target: int

    def __init__(self) -> None:
        self.paths = 0

    def depth_first_search(self, node: Node | None, path_sum: int) -> None:
        if node is None:
            return

        if path_sum == self.target:
            self.paths += 1

        if node.left:
            self.depth_first_search(node.left, path_sum + node.left.value)
        if node.right:
            self.depth_first_search(node.right, path_sum + node.right.value)

    def path_sum(self, node: Node | None, target: int | None = None) -> int:
        if node is None:
            return 0
        if target is not None:
            self.target = target

        self.depth_first_search(node, node.value)
        self.path_sum(node.left)
        self.path_sum(node.right)

        return self.paths


"""
Author  : Alexander Pantyukhin
Date    : November 2, 2022

Task:
Given the root of a binary tree, determine if it is a valid binary search
tree (BST).

A valid binary search tree is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Implementation notes:
Depth-first search approach.

leetcode: https://leetcode.com/problems/validate-binary-search-tree/

Let n is the number of nodes in tree
Runtime: O(n)
Space: O(1)
"""

from dataclasses import dataclass


@dataclass
class TreeNode:
    data: float
    left: TreeNode | None = None
    right: TreeNode | None = None


def is_binary_search_tree(root: TreeNode | None) -> bool:
    """
    >>> is_binary_search_tree(TreeNode(data=2,
    ...                                left=TreeNode(data=1),
    ...                                right=TreeNode(data=3))
    ...                                )
    True

    >>> is_binary_search_tree(TreeNode(data=0,
    ...                                left=TreeNode(data=-11),
    ...                                right=TreeNode(data=3))
    ...                                )
    True

    >>> is_binary_search_tree(TreeNode(data=5,
    ...                                left=TreeNode(data=1),
    ...                                right=TreeNode(data=4, left=TreeNode(data=3)))
    ...                      )
    False

    >>> is_binary_search_tree(TreeNode(data='a',
    ...                                left=TreeNode(data=1),
    ...                                right=TreeNode(data=4, left=TreeNode(data=3)))
    ...                      )
    Traceback (most recent call last):
     ...
    ValueError: Each node should be type of TreeNode and data should be float.

    >>> is_binary_search_tree(TreeNode(data=2,
    ...                                left=TreeNode([]),
    ...                                right=TreeNode(data=4, left=TreeNode(data=3)))
    ...                                )
    Traceback (most recent call last):
     ...
    ValueError: Each node should be type of TreeNode and data should be float.
    """

    # Validation
    def is_valid_tree(node: TreeNode | None) -> bool:
        """
        >>> is_valid_tree(None)
        True
        >>> is_valid_tree('abc')
        False
        >>> is_valid_tree(TreeNode(data='not a float'))
        False
        >>> is_valid_tree(TreeNode(data=1, left=TreeNode('123')))
        False
        """
        if node is None:
            return True

        if not isinstance(node, TreeNode):
            return False

        try:
            float(node.data)
        except (TypeError, ValueError):
            return False

        return is_valid_tree(node.left) and is_valid_tree(node.right)

    if not is_valid_tree(root):
        raise ValueError(
            "Each node should be type of TreeNode and data should be float."
        )

    def is_binary_search_tree_recursive_check(
        node: TreeNode | None, left_bound: float, right_bound: float
    ) -> bool:
        """
        >>> is_binary_search_tree_recursive_check(None)
        True
        >>> is_binary_search_tree_recursive_check(TreeNode(data=1), 10, 20)
        False
        """

        if node is None:
            return True

        return (
            left_bound < node.data < right_bound
            and is_binary_search_tree_recursive_check(node.left, left_bound, node.data)
            and is_binary_search_tree_recursive_check(
                node.right, node.data, right_bound
            )
        )

    return is_binary_search_tree_recursive_check(root, -float("inf"), float("inf"))




def merge_two_binary_trees(tree1: Node | None, tree2: Node | None) -> Node | None:
    """
    Returns root node of the merged tree.

    >>> tree1 = Node(5)
    >>> tree1.left = Node(6)
    >>> tree1.right = Node(7)
    >>> tree1.left.left = Node(2)
    >>> tree2 = Node(4)
    >>> tree2.left = Node(5)
    >>> tree2.right = Node(8)
    >>> tree2.left.right = Node(1)
    >>> tree2.right.right = Node(4)
    >>> merged_tree = merge_two_binary_trees(tree1, tree2)
    >>> print_preorder(merged_tree)
    9
    11
    2
    1
    15
    4
    """
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    tree1.value = tree1.value + tree2.value
    tree1.left = merge_two_binary_trees(tree1.left, tree2.left)
    tree1.right = merge_two_binary_trees(tree1.right, tree2.right)
    return tree1


def print_preorder(root: Node | None) -> None:
    """
    Print pre-order traversal of the tree.

    >>> root = Node(1)
    >>> root.left = Node(2)
    >>> root.right = Node(3)
    >>> print_preorder(root)
    1
    2
    3
    >>> print_preorder(root.right)
    3
    """
    if root:
        print(root.value)
        print_preorder(root.left)
        print_preorder(root.right)
