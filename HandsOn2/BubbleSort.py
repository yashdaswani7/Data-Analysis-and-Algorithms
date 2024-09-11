# Bubble Sort Algorithm
# ID: 1002257766
# Name: Yash Daswani

import random

def bubble_sort(arr):
    """Perform bubble sort on the array."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If the array is already sorted, exit early
        if not swapped:
            break

def main():
    """Run various test cases to validate the bubble sort algorithm."""
    
    # Test Case 1: Standard array
    standard_array = [10, 7, 3, -9, 3, -19, 5, 6]
    bubble_sort(standard_array)
    print("Test Case 1 - Standard array:", standard_array)
    
    # Test Case 2: Empty array
    empty_array = []
    bubble_sort(empty_array)
    print("Test Case 2 - Empty array:", empty_array)
    
    # Test Case 3: Array with a single element
    single_element_array = [2168]
    bubble_sort(single_element_array)
    print("Test Case 3 - Single element array:", single_element_array)
    
    # Test Case 4: Sorted array - Ascending
    ascending_sorted_array = [18, 32, 41, 88, 93]
    bubble_sort(ascending_sorted_array)
    print("Test Case 4 - Ascending sorted array:", ascending_sorted_array)
    
    # Test Case 5: Sorted array - Descending
    descending_sorted_array = [814, 721, 566, 472, 363, 15]
    bubble_sort(descending_sorted_array)
    print("Test Case 5 - Descending sorted array:", descending_sorted_array)
    
    # Test Case 6: All identical elements
    identical_elements_array = [8288, 8288, 8288, 8288]
    bubble_sort(identical_elements_array)
    print("Test Case 6 - Identical elements array:", identical_elements_array)
    
    # Test Case 7: Array with negative numbers
    negative_numbers_array = [-3, -1, -7, -4, -2]
    bubble_sort(negative_numbers_array)
    print("Test Case 7 - Negative numbers array:", negative_numbers_array)

    # Test Case 8: Large array with random values
    large_array = [random.randint(-23000, 23000) for _ in range(20)]
    print("Test Case 8 - Large random array before sorting:", large_array)
    bubble_sort(large_array)
    print("Test Case 8 - Large random array after sorting:", large_array)

if __name__ == "__main__":
    main()
