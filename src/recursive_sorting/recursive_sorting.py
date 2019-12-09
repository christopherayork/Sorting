# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    result = []
    while len(left) or len(right):
        if len(left) <= 0:
            result.append(right.pop(0))
        elif len(right) <= 0:
            result.append(left.pop(0))
        elif left[0] <= right[0]:
            result.append(left.pop(0))
        elif left[0] >= right[0]:
            result.append(right.pop(0))


# TO-DO: implement the Merge Sort function below USING RECURSION
import math


def merge_sort(l):
    if len(l) <= 1: return l
    middle = math.floor(len(l) / 2)
    left = merge_sort(l[0:middle])
    right = merge_sort(l[middle:])
    result = []
    while len(left) or len(right):
        if len(left) <= 0:
            result.append(right.pop(0))
        elif len(right) <= 0:
            result.append(left.pop(0))
        elif left[0] <= right[0]:
            result.append(left.pop(0))
        elif left[0] >= right[0]:
            result.append(right.pop(0))
    return result


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
