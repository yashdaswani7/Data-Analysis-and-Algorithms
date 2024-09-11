# Merge function to combine two sorted sub-arrays
def merge(left, right):
    sorted_array = []
    i = j = 0

    # Compare elements from both sub-arrays and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append remaining elements from the left or right sub-array
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Merge sort function
def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

# Given array
arr = [5, 2, 4, 7, 1, 3, 2, 6]

# Perform merge sort on the array
sorted_array = merge_sort(arr)

# Output the sorted array
print("Sorted array:", sorted_array)
