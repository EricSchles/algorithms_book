def simple_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def rec_simple_sort(arr, i):
    if i == len(arr):
        return arr
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    return rec_simple_sort(arr, i+1)

def bin_sort(arr, i):
    if len(arr) == 1
        return arr
    mid = len(arr)//2

a = list(range(10))
a = a[::-1]
print(rec_simple_sort(a, 0))

    

