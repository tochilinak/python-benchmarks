def bubble_sort(list_data: list, length: int = 0) -> list:
    """
    It is similar is bubble sort but recursive.
    :param list_data: mutable ordered sequence of elements
    :param length: length of list data
    :return: the same list in ascending order

    >>> bubble_sort([0, 5, 2, 3, 2], 5)
    [0, 2, 2, 3, 5]

    >>> bubble_sort([], 0)
    []

    >>> bubble_sort([-2, -45, -5], 3)
    [-45, -5, -2]

    >>> bubble_sort([-23, 0, 6, -4, 34], 5)
    [-23, -4, 0, 6, 34]

    >>> bubble_sort([-23, 0, 6, -4, 34], 5) == sorted([-23, 0, 6, -4, 34])
    True

    >>> bubble_sort(['z','a','y','b','x','c'], 6)
    ['a', 'b', 'c', 'x', 'y', 'z']

    >>> bubble_sort([1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6])
    [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
    """
    length = length or len(list_data)
    swapped = False
    for i in range(length - 1):
        if list_data[i] > list_data[i + 1]:
            list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
            swapped = True

    return list_data if not swapped else bubble_sort(list_data, length - 1)



def rec_insertion_sort(collection: list, n: int):
    """
    Given a collection of numbers and its length, sorts the collections
    in ascending order

    :param collection: A mutable collection of comparable elements
    :param n: The length of collections

    >>> col = [1, 2, 1]
    >>> rec_insertion_sort(col, len(col))
    >>> col
    [1, 1, 2]

    >>> col = [2, 1, 0, -1, -2]
    >>> rec_insertion_sort(col, len(col))
    >>> col
    [-2, -1, 0, 1, 2]

    >>> col = [1]
    >>> rec_insertion_sort(col, len(col))
    >>> col
    [1]
    """
    # Checks if the entire collection has been sorted
    if len(collection) <= 1 or n <= 1:
        return

    insert_next(collection, n - 1)
    rec_insertion_sort(collection, n - 1)


def insert_next(collection: list, index: int):
    """
    Inserts the '(index-1)th' element into place

    >>> col = [3, 2, 4, 2]
    >>> insert_next(col, 1)
    >>> col
    [2, 3, 4, 2]

    >>> col = [3, 2, 3]
    >>> insert_next(col, 2)
    >>> col
    [3, 2, 3]

    >>> col = []
    >>> insert_next(col, 1)
    >>> col
    []
    """
    # Checks order between adjacent elements
    if index >= len(collection) or collection[index - 1] <= collection[index]:
        return

    # Swaps adjacent elements since they are not in ascending order
    collection[index - 1], collection[index] = (
        collection[index],
        collection[index - 1],
    )

    insert_next(collection, index + 1)



def merge(arr: list[int]) -> list[int]:
    """Return a sorted array.
    >>> merge([10,9,8,7,6,5,4,3,2,1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge([1,2,3,4,5,6,7,8,9,10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge([10,22,1,2,3,9,15,23])
    [1, 2, 3, 9, 10, 15, 22, 23]
    >>> merge([100])
    [100]
    >>> merge([])
    []
    """
    if len(arr) > 1:
        middle_length = len(arr) // 2  # Finds the middle of the array
        left_array = arr[
            :middle_length
        ]  # Creates an array of the elements in the first half.
        right_array = arr[
            middle_length:
        ]  # Creates an array of the elements in the second half.
        left_size = len(left_array)
        right_size = len(right_array)
        merge(left_array)  # Starts sorting the left.
        merge(right_array)  # Starts sorting the right
        left_index = 0  # Left Counter
        right_index = 0  # Right Counter
        index = 0  # Position Counter
        while (
            left_index < left_size and right_index < right_size
        ):  # Runs until the lowers size of the left and right are sorted.
            if left_array[left_index] < right_array[right_index]:
                arr[index] = left_array[left_index]
                left_index += 1
            else:
                arr[index] = right_array[right_index]
                right_index += 1
            index += 1
        while (
            left_index < left_size
        ):  # Adds the left over elements in the left half of the array
            arr[index] = left_array[left_index]
            left_index += 1
            index += 1
        while (
            right_index < right_size
        ):  # Adds the left over elements in the right half of the array
            arr[index] = right_array[right_index]
            right_index += 1
            index += 1
    return arr



def quick_sort(data: list) -> list:
    """
    >>> for data in ([2, 1, 0], [2.2, 1.1, 0], "quick_sort"):
    ...     quick_sort(data) == sorted(data)
    True
    True
    True
    """
    if len(data) <= 1:
        return data
    else:
        return [
            *quick_sort([e for e in data[1:] if e <= data[0]]),
            data[0],
            *quick_sort([e for e in data[1:] if e > data[0]]),
        ]



def stooge_sort(arr):
    """
    Examples:
    >>> stooge_sort([18.1, 0, -7.1, -1, 2, 2])
    [-7.1, -1, 0, 2, 2, 18.1]

    >>> stooge_sort([])
    []
    """
    stooge(arr, 0, len(arr) - 1)
    return arr


def stooge(arr, i, h):
    if i >= h:
        return

    # If first element is smaller than the last then swap them
    if arr[i] > arr[h]:
        arr[i], arr[h] = arr[h], arr[i]

    # If there are more than 2 elements in the array
    if h - i + 1 > 2:
        t = (int)((h - i + 1) / 3)

        # Recursively sort first 2/3 elements
        stooge(arr, i, (h - t))

        # Recursively sort last 2/3 elements
        stooge(arr, i + t, (h))

        # Recursively sort first 2/3 elements
        stooge(arr, i, (h - t))