def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, i):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)
    k = pivot_index - low + 1  # Number of elements in the left partition

    if i == k:
        return arr[pivot_index]
    elif i < k:
        return quickselect(arr, low, pivot_index - 1, i)
    else:
        return quickselect(arr, pivot_index + 1, high, i - k)

# Example usage:
arr = [3, 2, 1, 5, 4]
i = 3  # Find the 3rd smallest element
ith_element = quickselect(arr, 0, len(arr) - 1, i)
print(f"The {i}rd smallest element is {ith_element}")
