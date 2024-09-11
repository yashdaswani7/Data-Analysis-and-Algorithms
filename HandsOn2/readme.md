**Author**: Yash Daswani  
**ID**: 1002257766

# Selection Sort Algorithm: Correctness Proof

## Selection Sort Algorithm

**Description**:
1. Iterate over the array from the beginning to the end.
2. For each position, find the smallest element in the unsorted portion.
3. Swap this smallest element with the element at the current position.
4. Repeat until the entire array is sorted.

## Correctness Proof

To prove the correctness of Selection Sort, we will demonstrate the following:

### 1. Partial Correctness

- **Base Case**: Initially, the sorted portion is empty. An empty prefix is considered sorted.

- **Inductive Hypothesis**: Assume that after the \(k\)-th iteration, the first \(k\) elements are sorted, and the remaining elements are unsorted.

- **Finding the Minimum**: During the \(k\)-th iteration, find the smallest element in the unsorted portion (from index \(k\) to \(n-1\)) and place it in the \(k\)-th position. This ensures the first \(k+1\) elements are sorted.

- **Swap Operation**: Swapping the smallest element with the element at the \(k\)-th position maintains the sorted order of the first \(k\) elements.

- **Conclusion**: After \(n-1\) iterations, the entire array is sorted.

### 2. Termination

- **Number of Iterations**: The algorithm performs \(n-1\) iterations, where \(n\) is the number of elements.

- **Loop Behavior**: Each iteration reduces the unsorted portion by 1, and processes the entire array in this manner.

- **Termination**: After \(n-1\) iterations, the array is fully sorted, and the algorithm terminates.

## Conclusion

Selection Sort is correct because:

1. **Partial Correctness**: The sorted portion of the array grows with each iteration, and the entire array is sorted after \(n-1\) iterations.
2. **Termination**: The algorithm completes after a fixed number of iterations and ensures the entire array is sorted.

Therefore, Selection Sort is a correct and complete sorting algorithm.
