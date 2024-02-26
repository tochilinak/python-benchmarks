from typing import Any


"""
Bead sort only works for sequences of non-negative integers.
https://en.wikipedia.org/wiki/Bead_sort
"""


def bead_sort(sequence: list) -> list:
    """
    >>> bead_sort([6, 11, 12, 4, 1, 5])
    [1, 4, 5, 6, 11, 12]

    >>> bead_sort([9, 8, 7, 6, 5, 4 ,3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> bead_sort([5, 0, 4, 3])
    [0, 3, 4, 5]

    >>> bead_sort([8, 2, 1])
    [1, 2, 8]

    >>> bead_sort([1, .9, 0.0, 0, -1, -.9])
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be list of non-negative integers

    >>> bead_sort("Hello world")
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be list of non-negative integers
    """
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("Sequence must be list of non-negative integers")
    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence


"""
This is a pure Python implementation of the binary insertion sort algorithm

For doctests run following command:
python -m doctest -v binary_insertion_sort.py
or
python3 -m doctest -v binary_insertion_sort.py

For manual testing run:
python binary_insertion_sort.py
"""


def binary_insertion_sort(collection: list) -> list:
    """Pure implementation of the binary insertion sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> binary_insertion_sort([0, 4, 1234, 4, 1])
    [0, 1, 4, 4, 1234]
    >>> binary_insertion_sort([]) == sorted([])
    True
    >>> binary_insertion_sort([-1, -2, -3]) == sorted([-1, -2, -3])
    True
    >>> lst = ['d', 'a', 'b', 'e', 'c']
    >>> binary_insertion_sort(lst) == sorted(lst)
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> binary_insertion_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> binary_insertion_sort(collection) == sorted(collection)
    True
    """

    n = len(collection)
    for i in range(1, n):
        val = collection[i]
        low = 0
        high = i - 1

        while low <= high:
            mid = (low + high) // 2
            if val < collection[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -1):
            collection[j] = collection[j - 1]
        collection[low] = val
    return collection



def bubble_sort(collection: list[Any]) -> list[Any]:
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    >>> bubble_sort([]) == sorted([])
    True
    >>> bubble_sort([-2, -45, -5]) == sorted([-2, -45, -5])
    True
    >>> bubble_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    >>> bubble_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> bubble_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> bubble_sort(collection) == sorted(collection)
    True
    """
    length = len(collection)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection



def bucket_sort(my_list: list, bucket_count: int = 10) -> list:
    """
    >>> data = [-1, 2, -5, 0]
    >>> bucket_sort(data) == sorted(data)
    True
    >>> data = [9, 8, 7, 6, -12]
    >>> bucket_sort(data) == sorted(data)
    True
    >>> data = [.4, 1.2, .1, .2, -.9]
    >>> bucket_sort(data) == sorted(data)
    True
    >>> bucket_sort([]) == sorted([])
    True
    >>> data = [-1e10, 1e10]
    >>> bucket_sort(data) == sorted(data)
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 50)
    >>> bucket_sort(collection) == sorted(collection)
    True
    """

    if len(my_list) == 0 or bucket_count <= 0:
        return []

    min_value, max_value = min(my_list), max(my_list)
    bucket_size = (max_value - min_value) / bucket_count
    buckets: list[list] = [[] for _ in range(bucket_count)]

    for val in my_list:
        index = min(int((val - min_value) / bucket_size), bucket_count - 1)
        buckets[index].append(val)

    return [val for bucket in buckets for val in sorted(bucket)]



""" https://en.wikipedia.org/wiki/Cocktail_shaker_sort """


def cocktail_shaker_sort(unsorted: list) -> list:
    """
    Pure implementation of the cocktail shaker sort algorithm in Python.
    >>> cocktail_shaker_sort([4, 5, 2, 1, 2])
    [1, 2, 2, 4, 5]

    >>> cocktail_shaker_sort([-4, 5, 0, 1, 2, 11])
    [-4, 0, 1, 2, 5, 11]

    >>> cocktail_shaker_sort([0.1, -2.4, 4.4, 2.2])
    [-2.4, 0.1, 2.2, 4.4]

    >>> cocktail_shaker_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]

    >>> cocktail_shaker_sort([-4, -5, -24, -7, -11])
    [-24, -11, -7, -5, -4]
    """
    for i in range(len(unsorted) - 1, 0, -1):
        swapped = False

        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                swapped = True

        for j in range(i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                swapped = True

        if not swapped:
            break
    return unsorted



def double_sort(lst):
    """This sorting algorithm sorts an array using the principle of bubble sort,
    but does it both from left to right and right to left.
    Hence, it's called "Double sort"
    :param collection: mutable ordered sequence of elements
    :return: the same collection in ascending order
    Examples:
    >>> double_sort([-1 ,-2 ,-3 ,-4 ,-5 ,-6 ,-7])
    [-7, -6, -5, -4, -3, -2, -1]
    >>> double_sort([])
    []
    >>> double_sort([-1 ,-2 ,-3 ,-4 ,-5 ,-6])
    [-6, -5, -4, -3, -2, -1]
    >>> double_sort([-3, 10, 16, -42, 29]) == sorted([-3, 10, 16, -42, 29])
    True
    """
    no_of_elements = len(lst)
    for _ in range(
        0, int(((no_of_elements - 1) / 2) + 1)
    ):  # we don't need to traverse to end of list as
        for j in range(0, no_of_elements - 1):
            if (
                lst[j + 1] < lst[j]
            ):  # applying bubble sort algorithm from left to right (or forwards)
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp
            if (
                lst[no_of_elements - 1 - j] < lst[no_of_elements - 2 - j]
            ):  # applying bubble sort algorithm from right to left (or backwards)
                temp = lst[no_of_elements - 1 - j]
                lst[no_of_elements - 1 - j] = lst[no_of_elements - 2 - j]
                lst[no_of_elements - 2 - j] = temp
    return lst



def exchange_sort(numbers: list[int]) -> list[int]:
    """
    Uses exchange sort to sort a list of numbers.
    Source: https://en.wikipedia.org/wiki/Sorting_algorithm#Exchange_sort
    >>> exchange_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> exchange_sort([-1, -2, -3])
    [-3, -2, -1]
    >>> exchange_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> exchange_sort([0, 10, -2, 5, 3])
    [-2, 0, 3, 5, 10]
    >>> exchange_sort([])
    []
    """
    numbers_length = len(numbers)
    for i in range(numbers_length):
        for j in range(i + 1, numbers_length):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers



def gnome_sort(lst: list) -> list:
    """
    Pure implementation of the gnome sort algorithm in Python

    Take some mutable ordered collection with heterogeneous comparable items inside as
    arguments, return the same collection ordered by ascending.

    Examples:
    >>> gnome_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> gnome_sort([])
    []

    >>> gnome_sort([-2, -5, -45])
    [-45, -5, -2]

    >>> "".join(gnome_sort(list(set("Gnomes are stupid!"))))
    ' !Gadeimnoprstu'
    """
    if len(lst) <= 1:
        return lst

    i = 1

    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
            if i == 0:
                i = 1

    return lst



"""
https://en.wikipedia.org/wiki/Shellsort#Pseudocode
"""


def shell_sort(collection):
    """Pure implementation of shell sort algorithm in Python
    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending

    >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> shell_sort([])
    []
    >>> shell_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # Marcin Ciura's gap sequence

    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(collection)):
            insert_value = collection[i]
            j = i
            while j >= gap and collection[j - gap] > insert_value:
                collection[j] = collection[j - gap]
                j -= gap
            if j != i:
                collection[j] = insert_value
    return collection



def selection_sort(collection):
    """Pure implementation of the selection sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending


    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        if least != i:
            collection[least], collection[i] = (collection[i], collection[least])
    return collection



def comb_sort(data: list) -> list:
    """Pure implementation of comb sort algorithm in Python
    :param data: mutable collection with comparable items
    :return: the same collection in ascending order
    Examples:
    >>> comb_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> comb_sort([])
    []
    >>> comb_sort([99, 45, -7, 8, 2, 0, -15, 3])
    [-15, -7, 0, 2, 3, 8, 45, 99]
    """
    shrink_factor = 1.3
    gap = len(data)
    completed = False

    while not completed:
        # Update the gap value for a next comb
        gap = int(gap / shrink_factor)
        if gap <= 1:
            completed = True

        index = 0
        while index + gap < len(data):
            if data[index] > data[index + gap]:
                # Swap values
                data[index], data[index + gap] = data[index + gap], data[index]
                completed = False
            index += 1

    return data