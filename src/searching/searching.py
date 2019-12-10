# STRETCH: implement Linear Search				
def linear_search(arr, target):
    # TO-DO: add missing code
    result = -1
    counter = 0
    for i in arr:
        if i == target:
            result = counter
            break
        counter += 1
    return result  # not found


# STRETCH: write an iterative implementation of Binary Search
import math


def binary_search(arr, target):
    if len(arr) < 1: return -1
    low = 0
    high = len(arr) - 1
    middle = None
    while True:
        middle = math.floor((high + low) / 2)
        if arr[middle] == target:
            return middle
        elif low == high:
            return -1
        elif arr[middle] > target:
            high = middle - 1
        elif arr[middle] < target:
            low = middle + 1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
