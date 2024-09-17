def combine_sorted_arrays(list1, list2):
    pointer1, pointer2 = 0, 0
    result = []
    
    # Two-pointer technique to merge two sorted arrays
    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1] < list2[pointer2]:
            result.append(list1[pointer1])
            pointer1 += 1
        else:
            result.append(list2[pointer2])
            pointer2 += 1

    # Append the remaining elements of list1 or list2
    while pointer1 < len(list1):
        result.append(list1[pointer1])
        pointer1 += 1
    while pointer2 < len(list2):
        result.append(list2[pointer2])
        pointer2 += 1

    return result

def merge_k_sorted_arrays(k, n, array1, array2, array3):
    sorted_arrays = [array1, array2, array3]
    
    while len(sorted_arrays) > 1:
        new_sorted_list = []
        
        # Merge arrays in pairs
        for index in range(0, len(sorted_arrays), 2):
            if index + 1 < len(sorted_arrays):
                new_sorted_list.append(combine_sorted_arrays(sorted_arrays[index], sorted_arrays[index + 1]))
            else:
                new_sorted_list.append(sorted_arrays[index])
        
        sorted_arrays = new_sorted_list
    
    return sorted_arrays[0]

def main():
    # First example
    k = 3
    n = 4
    array1 = [1, 3, 5, 7]
    array2 = [2, 4, 6, 8]
    array3 = [0, 9, 10, 11]
    
    result = merge_k_sorted_arrays(k, n, array1, array2, array3)
    print(result)
    # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    # Second example
    k = 3
    n = 3
    array1 = [1, 3, 7]
    array2 = [2, 4, 8]
    array3 = [9, 10, 11]
    
    result = merge_k_sorted_arrays(k, n, array1, array2, array3)
    print(result)
    # Output: [1, 2, 3, 4, 7, 8, 9, 10, 11]

if __name__ == "__main__":
    main()
