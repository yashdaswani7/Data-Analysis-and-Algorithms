# Selection Sort Algorithm
# ID: 1002257766
# Name: Yash Daswani

# Selection sort algorithm
def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        mini = i
        # Loop to get the minimum index from the array
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        # Swap ith element with minimum value
        arr[i], arr[mini] = arr[mini], arr[i]

def main():
    # Test Case 1: Standard array
    arr1 = [10, 7, 3, -9, 3, -19, 5, 6]
    selectionSort(arr1)
    print("Test Case 1:", arr1)
    
    # Test Case 2: Empty array
    arr2 = []
    selectionSort(arr2)
    print("Test Case 2:", arr2)
    
    # Test Case 3: Array with a single element
    arr3 = [2168]
    selectionSort(arr3)
    print("Test Case 3:", arr3)
    
    # Test Case 4: Sorted array - Ascending
    arr4 = [18, 32, 41, 88, 93]
    selectionSort(arr4)
    print("Test Case 4:", arr4)
    
    # Test Case 5: Sorted array - Descending
    arr5 = [814, 721, 566, 472, 363, 15]
    selectionSort(arr5)
    print("Test Case 5:", arr5)
    
    # Test Case 6: All identical elements
    arr6 = [8288, 8288, 8288, 8288]
    selectionSort(arr6)
    print("Test Case 6:", arr6)
    
if __name__ == "__main__":
    main()
