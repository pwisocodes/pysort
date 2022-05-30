import logging
from pysort.helper import timing


@timing
def quicksort(array):
    """Funtion to perform quicksort

    Args:
        array (list): list of numericals that should be sorted
    """
    left = 0
    right = len(array) - 1
    __quicksort(left, right, array)
    return array


def __quicksort(left, right, array):
    """Inner quicksort function, which will find the pivot element and do recursive calls on itself

    Args:
        left (_type_): _description_
        right (_type_): _description_
        array (_type_): _description_
    """
    if left < right:

        div = partition(array, left, right)
        __quicksort(left, (div - 1), array)
        __quicksort((div + 1), right, array)


def partition(array, left, right):
    """Function to find the regular partition position

    Args:
        array (list): array of numerical integers
        left (index): left index element
        right (index): right index element

    Returns:
        ptr: numeical index from where the partition is done
    """
    pivot, ptr = array[right], left
    for i in range(left, right):
        if array[i] <= pivot:
            logging.debug(
                f"Array element:{array[i]} smaller than pivot element: {pivot}"
            )
            array[i], array[ptr] = array[ptr], array[i]
            ptr += 1

    logging.debug(
        f"Change element: {ptr} with: {right} ; Pivot element: {pivot}"
    )
    array[ptr], array[right] = array[right], array[ptr]
    return ptr
