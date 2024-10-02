## Name: Yash Daswani  
## Student ID: 1002257766  

# Average Runtime Complexity of Non-Random Pivot Quicksort
### Deriving the Average Case Time Complexity for Non-Random Quicksort

To derive the average case time complexity of the non-random pivot version of Quicksort, we can approach it mathematically. While Quicksort generally performs well with random pivots, using a fixed pivot (such as always picking the first or last element) allows us to analyze the complexity as follows:

1. **Divide and Conquer Approach**: Each partitioning step divides the array into two subarrays. The efficiency of the algorithm is highly dependent on how evenly the pivot divides the array.

2. **Recursive Relation**: The time complexity can be described by the following recursive relation:  
   \[
   T(n) = T(k) + T(n - k - 1) + O(n)
   \]  
   Here, \( k \) represents the number of elements in one partition, and \( O(n) \) refers to the time required to perform the partitioning step.

3. **Average Case Partitioning**: On average, the pivot will split the array into two roughly equal subarrays. This leads to the following recurrence:  
   \[
   T(n) = 2T\left(\frac{n}{2}\right) + O(n)
   \]

4. **Applying the Master Theorem**: Using the Master Theorem to solve this recurrence, we conclude that:  
   \[
   T(n) = O(n \log n)
   \]

Thus, the average case time complexity for the non-random pivot version of Quicksort is \( O(n \log n) \).
