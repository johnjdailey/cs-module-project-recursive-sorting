# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    ix, jx, kx = 0, 0, 0

    while ix < len(arrA) and jx < len(arrB):
        if arrA[ix] < arrB[jx]:
            merged_arr[kx] = arrA[ix]
            ix += 1

        else:
            merged_arr[kx] = arrB[jx]
            jx += 1
        kx += 1

    while ix < len(arrA):
        merged_arr[kx] = arrA[ix]
        ix += 1
        kx += 1

    while jx < len(arrB):
        merged_arr[kx] = arrB[jx]
        jx += 1
        kx += 1

    return merged_arr
    

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    arrA = merge_sort(arr[:half])
    arrB = merge_sort(arr[half:])

    arr = merge(arrA, arrB)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    ix = start
    ax = start
    bx = mid

    while ix <= end and ax < mid and bx <= end:
        if ax >= mid or arr[bx] > arr[ax]:
            tmp = arr[ax]
            arr[ax] = arr[bx]
            ax += 1
            bx += 1
            mid += 1
            for jx in range(ax, mid):
                tmp, arr[jx] = arr[jx], tmp

        else:
            ax += 1

        ix +=1

    return arr


def merge_sort_in_place(arr, l, r):
    if r - l <= 1:
        if r >= 0 and arr[l] > arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            return

    mid = (r + l) // 2
    merge_sort_in_place(arr, l, mid - 1)
    merge_sort_in_place(arr, mid, r)

    merge_in_place(arr, l, mid, r)

    return
