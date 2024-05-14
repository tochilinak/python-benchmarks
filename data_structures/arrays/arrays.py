def permute_recursive(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations.

    >>> permute_recursive([1, 2, 3])
    [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
    """
    result: list[list[int]] = []
    if len(nums) == 0:
        return [[]]
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute_recursive(nums)
        for perm in permutations:
            perm.append(n)
        result.extend(permutations)
        nums.append(n)
    return result


def permute_backtrack(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations of the given list.

    >>> permute_backtrack([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """

    def backtrack(start: int) -> None:
        if start == len(nums) - 1:
            output.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack

    output: list[list[int]] = []
    backtrack(0)
    return output


"""
Author  : Alexander Pantyukhin
Date    : November 3, 2022

Implement the class of prefix sum with useful functions based on it.

"""


class PrefixSum:
    def __init__(self, array: list[int]) -> None:
        len_array = len(array)
        self.prefix_sum = [0] * len_array

        if len_array > 0:
            self.prefix_sum[0] = array[0]

        for i in range(1, len_array):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + array[i]

    def get_sum(self, start: int, end: int) -> int:
        """
        The function returns the sum of array from the start to the end indexes.
        Runtime : O(1)
        Space: O(1)

        >>> PrefixSum([1,2,3]).get_sum(0, 2)
        6
        >>> PrefixSum([1,2,3]).get_sum(1, 2)
        5
        >>> PrefixSum([1,2,3]).get_sum(2, 2)
        3
        >>> PrefixSum([1,2,3]).get_sum(2, 3)
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
        """
        if start == 0:
            return self.prefix_sum[end]

        return self.prefix_sum[end] - self.prefix_sum[start - 1]

    def contains_sum(self, target_sum: int) -> bool:
        """
        The function returns True if array contains the target_sum,
        False otherwise.

        Runtime : O(n)
        Space: O(n)

        >>> PrefixSum([1,2,3]).contains_sum(6)
        True
        >>> PrefixSum([1,2,3]).contains_sum(5)
        True
        >>> PrefixSum([1,2,3]).contains_sum(3)
        True
        >>> PrefixSum([1,2,3]).contains_sum(4)
        False
        >>> PrefixSum([1,2,3]).contains_sum(7)
        False
        >>> PrefixSum([1,-2,3]).contains_sum(2)
        True
        """

        sums = {0}
        for sum_item in self.prefix_sum:
            if sum_item - target_sum in sums:
                return True

            sums.add(sum_item)

        return False


"""
Calculate the Product Sum from a Special Array.
reference: https://dev.to/sfrasica/algorithms-product-sum-from-an-array-dc6

Python doctests can be run with the following command:
python -m doctest -v product_sum.py

Calculate the product sum of a "special" array which can contain integers or nested
arrays. The product sum is obtained by adding all elements and multiplying by their
respective depths.

For example, in the array [x, y], the product sum is (x + y). In the array [x, [y, z]],
the product sum is x + 2 * (y + z). In the array [x, [y, [z]]],
the product sum is x + 2 * (y + 3z).

Example Input:
[5, 2, [-7, 1], 3, [6, [-13, 8], 4]]
Output: 12

"""


def product_sum(arr: list[int | list], depth: int) -> int:
    """
    Recursively calculates the product sum of an array.

    The product sum of an array is defined as the sum of its elements multiplied by
    their respective depths.  If an element is a list, its product sum is calculated
    recursively by multiplying the sum of its elements with its depth plus one.

    Args:
        arr: The array of integers and nested lists.
        depth: The current depth level.

    Returns:
        int: The product sum of the array.

    Examples:
        >>> product_sum([1, 2, 3], 1)
        6
        >>> product_sum([-1, 2, [-3, 4]], 2)
        8
        >>> product_sum([1, 2, 3], -1)
        -6
        >>> product_sum([1, 2, 3], 0)
        0
        >>> product_sum([1, 2, 3], 7)
        42
        >>> product_sum((1, 2, 3), 7)
        42
        >>> product_sum({1, 2, 3}, 7)
        42
        >>> product_sum([1, -1], 1)
        0
        >>> product_sum([1, -2], 1)
        -1
        >>> product_sum([-3.5, [1, [0.5]]], 1)
        1.5

    """
    total_sum = 0
    for ele in arr:
        total_sum += product_sum(ele, depth + 1) if isinstance(ele, list) else ele
    return total_sum * depth


def product_sum_array(array: list[int | list]) -> int:
    """
    Calculates the product sum of an array.

    Args:
        array (List[Union[int, List]]): The array of integers and nested lists.

    Returns:
        int: The product sum of the array.

    Examples:
        >>> product_sum_array([1, 2, 3])
        6
        >>> product_sum_array([1, [2, 3]])
        11
        >>> product_sum_array([1, [2, [3, 4]]])
        47
        >>> product_sum_array([0])
        0
        >>> product_sum_array([-3.5, [1, [0.5]]])
        1.5
        >>> product_sum_array([1, -2])
        -1

    """
    return product_sum(array, 1)
