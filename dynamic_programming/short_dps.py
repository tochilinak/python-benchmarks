"""
Question:
You are given an array of distinct integers and you have to tell how many
different ways of selecting the elements from the array are there such that
the sum of chosen elements is equal to the target number tar.

Example

Input:
N = 3
target = 5
array = [1, 2, 5]

Output:
9

Approach:
The basic idea is to go over recursively to find the way such that the sum
of chosen elements is “tar”. For every element, we have two choices
    1. Include the element in our set of chosen elements.
    2. Don’t include the element in our set of chosen elements.
"""


def combination_sum_iv(n: int, array: list[int], target: int) -> int:
    """
    Function checks the all possible combinations, and returns the count
    of possible combination in exponential Time Complexity.

    >>> combination_sum_iv(3, [1,2,5], 5)
    9
    """

    def count_of_possible_combinations(target: int) -> int:
        if target < 0:
            return 0
        if target == 0:
            return 1
        return sum(count_of_possible_combinations(target - item) for item in array)

    return count_of_possible_combinations(target)


def combination_sum_iv_dp_array(n: int, array: list[int], target: int) -> int:
    """
    Function checks the all possible combinations, and returns the count
    of possible combination in O(N^2) Time Complexity as we are using Dynamic
    programming array here.

    >>> combination_sum_iv_dp_array(3, [1,2,5], 5)
    9
    """

    def count_of_possible_combinations_with_dp_array(
        target: int, dp_array: list[int]
    ) -> int:
        if target < 0:
            return 0
        if target == 0:
            return 1
        if dp_array[target] != -1:
            return dp_array[target]
        answer = sum(
            count_of_possible_combinations_with_dp_array(target - item, dp_array)
            for item in array
        )
        dp_array[target] = answer
        return answer

    dp_array = [-1] * (target + 1)
    return count_of_possible_combinations_with_dp_array(target, dp_array)


def combination_sum_iv_bottom_up(n: int, array: list[int], target: int) -> int:
    """
    Function checks the all possible combinations with using bottom up approach,
    and returns the count of possible combination in O(N^2) Time Complexity
    as we are using Dynamic programming array here.

    >>> combination_sum_iv_bottom_up(3, [1,2,5], 5)
    9
    """

    dp_array = [0] * (target + 1)
    dp_array[0] = 1

    for i in range(1, target + 1):
        for j in range(n):
            if i - array[j] >= 0:
                dp_array[i] += dp_array[i - array[j]]

    return dp_array[target]


"""
Author  : Mehdi ALAOUI

This is a pure Python implementation of Dynamic Programming solution to the longest
increasing subsequence of a given sequence.

The problem is  :
Given an array, to find the longest and increasing sub-array in that given array and
return it.
Example: [10, 22, 9, 33, 21, 50, 41, 60, 80] as input will return
         [10, 22, 33, 41, 60, 80] as output
"""


def longest_subsequence(array: list[int]) -> list[int]:  # This function is recursive
    """
    Some examples
    >>> longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [10, 22, 33, 41, 60, 80]
    >>> longest_subsequence([4, 8, 7, 5, 1, 12, 2, 3, 9])
    [1, 2, 3, 9]
    >>> longest_subsequence([9, 8, 7, 6, 5, 7])
    [8]
    >>> longest_subsequence([1, 1, 1])
    [1, 1, 1]
    >>> longest_subsequence([])
    []
    """
    array_length = len(array)
    # If the array contains only one element, we return it (it's the stop condition of
    # recursion)
    if array_length <= 1:
        return array
        # Else
    pivot = array[0]
    is_found = False
    i = 1
    longest_subseq: list[int] = []
    while not is_found and i < array_length:
        if array[i] < pivot:
            is_found = True
            temp_array = [element for element in array[i:] if element >= array[i]]
            temp_array = longest_subsequence(temp_array)
            if len(temp_array) > len(longest_subseq):
                longest_subseq = temp_array
        else:
            i += 1

    temp_array = [element for element in array[1:] if element >= pivot]
    temp_array = [pivot, *longest_subsequence(temp_array)]
    if len(temp_array) > len(longest_subseq):
        return temp_array
    else:
        return longest_subseq


import sys

"""
Dynamic Programming
Implementation of Matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""


def matrix_chain_order(array):
    n = len(array)
    matrix = [[0 for x in range(n)] for x in range(n)]
    sol = [[0 for x in range(n)] for x in range(n)]

    for chain_length in range(2, n):
        for a in range(1, n - chain_length + 1):
            b = a + chain_length - 1

            matrix[a][b] = sys.maxsize
            for c in range(a, b):
                cost = (
                    matrix[a][c] + matrix[c + 1][b] + array[a - 1] * array[c] * array[b]
                )
                if cost < matrix[a][b]:
                    matrix[a][b] = cost
                    sol[a][b] = c
    return matrix, sol


# Print order of matrix with Ai as Matrix
def print_optiomal_solution(optimal_solution, i, j):
    if i == j:
        print("A" + str(i), end=" ")
    else:
        print("(", end=" ")
        print_optiomal_solution(optimal_solution, i, optimal_solution[i][j])
        print_optiomal_solution(optimal_solution, optimal_solution[i][j] + 1, j)
        print(")", end=" ")


def max_product_subarray(numbers: list[int]) -> int:
    """
    Returns the maximum product that can be obtained by multiplying a
    contiguous subarray of the given integer list `nums`.

    Example:
    >>> max_product_subarray([2, 3, -2, 4])
    6
    >>> max_product_subarray((-2, 0, -1))
    0
    >>> max_product_subarray([2, 3, -2, 4, -1])
    48
    >>> max_product_subarray([-1])
    -1
    >>> max_product_subarray([0])
    0
    >>> max_product_subarray([])
    0
    >>> max_product_subarray("")
    0
    >>> max_product_subarray(None)
    0
    >>> max_product_subarray([2, 3, -2, 4.5, -1])
    Traceback (most recent call last):
        ...
    ValueError: numbers must be an iterable of integers
    >>> max_product_subarray("ABC")
    Traceback (most recent call last):
        ...
    ValueError: numbers must be an iterable of integers
    """
    if not numbers:
        return 0

    if not isinstance(numbers, (list, tuple)) or not all(
        isinstance(number, int) for number in numbers
    ):
        raise ValueError("numbers must be an iterable of integers")

    max_till_now = min_till_now = max_prod = numbers[0]

    for i in range(1, len(numbers)):
        # update the maximum and minimum subarray products
        number = numbers[i]
        if number < 0:
            max_till_now, min_till_now = min_till_now, max_till_now
        max_till_now = max(number, max_till_now * number)
        min_till_now = min(number, min_till_now * number)

        # update the maximum product found till now
        max_prod = max(max_prod, max_till_now)

    return max_prod


"""
The maximum subarray sum problem is the task of finding the maximum sum that can be
obtained from a contiguous subarray within a given array of numbers. For example, given
the array [-2, 1, -3, 4, -1, 2, 1, -5, 4], the contiguous subarray with the maximum sum
is [4, -1, 2, 1], so the maximum subarray sum is 6.

Kadane's algorithm is a simple dynamic programming algorithm that solves the maximum
subarray sum problem in O(n) time and O(1) space.

Reference: https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""
from collections.abc import Sequence


def max_subarray_sum(
    arr: Sequence[float], allow_empty_subarrays: bool = False
) -> float:
    """
    Solves the maximum subarray sum problem using Kadane's algorithm.
    :param arr: the given array of numbers
    :param allow_empty_subarrays: if True, then the algorithm considers empty subarrays

    >>> max_subarray_sum([2, 8, 9])
    19
    >>> max_subarray_sum([0, 0])
    0
    >>> max_subarray_sum([-1.0, 0.0, 1.0])
    1.0
    >>> max_subarray_sum([1, 2, 3, 4, -2])
    10
    >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    >>> max_subarray_sum([2, 3, -9, 8, -2])
    8
    >>> max_subarray_sum([-2, -3, -1, -4, -6])
    -1
    >>> max_subarray_sum([-2, -3, -1, -4, -6], allow_empty_subarrays=True)
    0
    >>> max_subarray_sum([])
    0
    """
    if not arr:
        return 0

    max_sum = 0 if allow_empty_subarrays else float("-inf")
    curr_sum = 0.0
    for num in arr:
        curr_sum = max(0 if allow_empty_subarrays else num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum


"""
You have m types of coins available in infinite quantities
where the value of each coins is given in the array S=[S0,... Sm-1]
Can you determine number of ways of making change for n units using
the given types of coins?
https://www.hackerrank.com/challenges/coin-change/problem
"""


def dp_count(s, n):
    """
    >>> dp_count([1, 2, 3], 4)
    4
    >>> dp_count([1, 2, 3], 7)
    8
    >>> dp_count([2, 5, 3, 6], 10)
    5
    >>> dp_count([10], 99)
    0
    >>> dp_count([4, 5, 6], 0)
    1
    >>> dp_count([1, 2, 3], -5)
    0
    """
    if n < 0:
        return 0
    # table[i] represents the number of ways to get to amount i
    table = [0] * (n + 1)

    # There is exactly 1 way to get to zero(You pick no coins).
    table[0] = 1

    # Pick all coins one by one and update table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for coin_val in s:
        for j in range(coin_val, n + 1):
            table[j] += table[j - coin_val]

    return table[n]



def minimum_cost_path(matrix: list[list[int]]) -> int:
    """
    Find the minimum cost traced by all possible paths from top left to bottom right in
    a given matrix

    >>> minimum_cost_path([[2, 1], [3, 1], [4, 2]])
    6

    >>> minimum_cost_path([[2, 1, 4], [2, 1, 3], [3, 2, 1]])
    7
    """

    # preprocessing the first row
    for i in range(1, len(matrix[0])):
        matrix[0][i] += matrix[0][i - 1]

    # preprocessing the first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]

    # updating the path cost for current position
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]


"""
Partition a set into two subsets such that the difference of subset sums is minimum
"""


def find_min(arr):
    n = len(arr)
    s = sum(arr)

    dp = [[False for x in range(s + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = True

    for i in range(1, s + 1):
        dp[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            dp[i][j] = dp[i][j - 1]

            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

    for j in range(int(s / 2), -1, -1):
        if dp[n][j] is True:
            diff = s - 2 * j
            break

    return diff


def is_sum_subset(arr: list[int], required_sum: int) -> bool:
    """
    >>> is_sum_subset([2, 4, 6, 8], 5)
    False
    >>> is_sum_subset([2, 4, 6, 8], 14)
    True
    """
    # a subset value says 1 if that subset sum can be formed else 0
    # initially no subsets can be formed hence False/0
    arr_len = len(arr)
    subset = [[False] * (required_sum + 1) for _ in range(arr_len + 1)]

    # for each arr value, a sum of zero(0) can be formed by not taking any element
    # hence True/1
    for i in range(arr_len + 1):
        subset[i][0] = True

    # sum is not zero and set is empty then false
    for i in range(1, required_sum + 1):
        subset[0][i] = False

    for i in range(1, arr_len + 1):
        for j in range(1, required_sum + 1):
            if arr[i - 1] > j:
                subset[i][j] = subset[i - 1][j]
            if arr[i - 1] <= j:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - arr[i - 1]]

    return subset[arr_len][required_sum]
