# TO-DO: Complete the selection_sort() function below

array1 = [3, 20, 1, 10, 2, 14, 18, 7]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap   -- Exchange operation
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


print(selection_sort(array1))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):  # <--- This will give us the two elements to compare
            if arr[j] > arr[j+1]:
                # <---- Simultaneous Assignment
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort(array1))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
