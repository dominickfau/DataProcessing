"""Contains an assortment of array sorting algorithms.
    Theses are from https://realpython.com/sorting-algorithms-python/
"""
from random import randint

def timeSort(array):
    """The Timsort algorithm is considered a hybrid sorting algorithm because it employs a
    best-of-both-worlds combination of insertion sort and merge sort.

    The main characteristic of Timsort is that it takes advantage of already-sorted elements
    that exist in most real-world datasets. These are called natural runs. The algorithm then
    iterates over the list, collecting the elements into runs and merging them into a single sorted list.
    
    Time complexity O(n log2n).

    Args:
        array (list): The list to sort.

    Returns:
        list: Returns the sorted list.
    """
    def _insertion_sort_modified(array, left=0, right=None):
        if right is None:
            right = len(array) - 1

        # Loop from the element indicated by
        # `left` until the element indicated by `right`
        for i in range(left + 1, right + 1):
            # This is the element we want to position in its
            # correct place
            key_item = array[i]

            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1

            # Run through the list of items (the left
            # portion of the array) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if the `key_item` is smaller than its adjacent values.
            while j >= left and array[j] > key_item:
                # Shift the value one position to the left
                # and reposition `j` to point to the next element
                # (from right to left)
                array[j + 1] = array[j]
                j -= 1

            # When you finish shifting the elements, position
            # the `key_item` in its correct location
            array[j + 1] = key_item

        return array

    min_run = 32
    n = len(array)

    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        _insertion_sort_modified(array, i, min((i + min_run - 1), n - 1))

    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `midpoint + 1`, while the `right` array should
            # go from `midpoint + 1` to `end + 1`.
            merged_array = _merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            # Finally, put the merged array back into
            # your array
            array[start:start + len(merged_array)] = merged_array

        # Each iteration should double the size of your arrays
        size *= 2

    return array


def quickSort(array):
    """Just like merge sort, the quicksort algorithm applies the divide-and-conquer principle
    to divide the input array into two lists, the first with small items and the second with
    large items. The algorithm then sorts both lists recursively until the resultant list is completely sorted.

    Dividing the input list is referred to as partitioning the list. Quicksort first selects a pivot
    element and partitions the list around the pivot, putting every smaller element into a low
    array and every larger element into a high array.

    Putting every element from the low list to the left of the pivot and every element from the high
    list to the right positions the pivot precisely where it needs to be in the final sorted list.
    This means that the function can now recursively apply the same procedure to low and then high
    until the entire list is sorted.
    
    Time complexity O(n log2n).

    Args:
        array (list): The list to sort.

    Returns:
        list: Returns the sorted list.
    """
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quickSort(low) + same + quickSort(high)


def _merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def mergeSort(array):
    """Merge sort is a very efficient sorting algorithm. It’s based on the divide-and-conquer approach.
    
    Divide-and-conquer algorithms typically follow the same structure:
        1. The original input is broken into several parts, each one representing a subproblem that’s similar to the original but simpler.
        2. Each subproblem is solved recursively.
        3. The solutions to all the subproblems are combined into a single overall solution.

    Time complexity O(n log2n).

    Args:
        array (list): The list to sort.

    Returns:
        list: Returns the sorted list.
    """
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return _merge(
        left=mergeSort(array[:midpoint]),
        right=mergeSort(array[midpoint:]))


def bubbleSort(array):
    """Bubble sort consists of making multiple passes through a list,
    comparing elements one by one, and swapping adjacent items that are out of order.

    Time complexity O(n2).

    Args:
        array (list): The list to sort.

    Returns:
        list: Returns the sorted list.
    """
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array


def insertionSort(array):
    """Like bubble sort, the insertion sort algorithm is straightforward to implement and understand.
    But unlike bubble sort, it builds the sorted list one element at a time by comparing each item
    with the rest of the list and inserting it into its correct position.
    This “insertion” procedure gives the algorithm its name.

    Time complexity O(n2).

    Args:
        array (list): The list to sort.

    Returns:
        list: Returns the sorted list.
    """
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array