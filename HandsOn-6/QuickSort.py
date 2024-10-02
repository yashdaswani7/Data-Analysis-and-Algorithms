import random

# Non-Random Pivot Quicksort
def partition(arr, start, end):
    pivot = arr[start]
    smaller_index = start + 1  
    
    for current in range(start + 1, end + 1):
        if arr[current] < pivot:
            arr[smaller_index], arr[current] = arr[current], arr[smaller_index]
            smaller_index += 1
    
    arr[start], arr[smaller_index - 1] = arr[smaller_index - 1], arr[start]
    return smaller_index - 1

def quicksort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end)

# Random Pivot Quicksort
def partition_with_random_pivot(arr, start, end):
    random_pivot_index = random.randint(start, end)
    arr[start], arr[random_pivot_index] = arr[random_pivot_index], arr[start]
    return partition(arr, start, end)

def quicksort_with_random_pivot(arr, start, end):
    if start < end:
        pivot_index = partition_with_random_pivot(arr, start, end)
        quicksort_with_random_pivot(arr, start, pivot_index - 1)
        quicksort_with_random_pivot(arr, pivot_index + 1, end)

# Test cases for both quicksort implementations
def test_quick_sort():
    test_cases = [
        {"name": "All Positive Numbers", "data": [12, 4, 78, 23, 45, 67, 89]},
        {"name": "Includes Negative Numbers", "data": [0, -5, 3, -2, 8, -9]},
        {"name": "Already Sorted", "data": [1, 2, 3, 4, 5, 6, 7, 8]},
        {"name": "Reverse Sorted", "data": [9, 8, 7, 6, 5, 4, 3]},
        {"name": "Mixed Data", "data": [3, -2, 0, 999, 432, -999, 123]},
        {"name": "Duplicate Values", "data": [8, 8, 3, 3, 9, 9, 1, 1]},
        {"name": "Single Element", "data": [5]},
        {"name": "Empty Array", "data": []},
        {"name": "Two Elements (Sorted)", "data": [4, 5]},
        {"name": "Two Elements (Unsorted)", "data": [5, 4]}
    ]

    for test_case in test_cases:
        arr = test_case["data"]
        arr_copy = arr.copy()

        print(f"\nTest Case: {test_case['name']}")
        print(f"Original Array: {arr_copy}")

        # Non-Random Pivot quicksort
        arr_copy = arr.copy()
        quicksort(arr_copy, 0, len(arr_copy) - 1)
        print(f"Sorted (Non-Random Pivot): {arr_copy}")

        # Random Pivot quicksort
        arr_copy = arr.copy()
        quicksort_with_random_pivot(arr_copy, 0, len(arr_copy) - 1)
        print(f"Sorted (Random Pivot): {arr_copy}")
        print("-" * 50)

if __name__ == "__main__":
    test_quick_sort()
