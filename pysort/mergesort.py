from collections import deque
from pysort.helper import timing
import queue
import logging


@timing
def mergesort(array):
    """ Function executes the mergesort algorithm

    Args:
        array (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(array) <= 1:
        return array
    else:
        if array is not None:
            mid_element = round(len(array) / 2)

            l_list = deque(mergesort(array[:mid_element]))
            r_list = deque(mergesort(array[mid_element:]))

            result = __merge(l_list, r_list)

        return result


def __merge(list_num1: queue, list_num2: queue):
    result = []
    logging.debug(f"List 1: {list(list_num1)}, List 2: {list(list_num2)}\n")
    while (len(list_num1) > 0) and (len(list_num2) > 0):
        if list_num1[0] <= list_num2[0]:
            result.append(list_num1.popleft())
        else:
            result.append(list_num2.popleft())

    while len(list_num1) > 0:
        result.append(list_num1.popleft())
    while len(list_num2) > 0:
        result.append(list_num2.popleft())

    return result
