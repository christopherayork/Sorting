# TO-DO: Complete the selection_sort() function below 
def selection_sort(l):
    # loop through n-1 elements
    if len(l) <= 1:
        return l
    smallest = 0
    r = l[:]
    pos = 0
    while pos < (len(r) - 1):
        smallest = pos
        for i in range(pos, len(r)):
            if r[smallest] > r[i]:
                smallest = i
        if r[pos] > r[smallest]:
            tmp = r[pos]
            r[pos] = r[smallest]
            r[smallest] = tmp
        pos += 1
    return r


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(l):
    if len(l) <= 1:
        return l
    r = l[:]
    changed = False
    last = False
    while True:
        changed = False
        for i in range(0, len(r) - 1):
            if r[i] > r[i + 1]:
                tmp = r[i]
                r[i] = r[i + 1]
                r[i + 1] = tmp
                changed = True
                continue
        if not changed and last:
            break
        elif not changed:
            last = True
    return r


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr