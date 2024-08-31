def selection_sort(arr):
    for i in range(len(arr)):
        pivot = i
        for j in range(i+1, len(arr)):
            if arr[pivot] > arr[j]:
                pivot = j
        arr[i], arr[pivot] = arr[pivot], arr[i]
    return arr

print(selection_sort([13, 4, 67, 23, 18, 45, 15, 3]))            