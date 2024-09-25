from typing import TypeVar

T = TypeVar('T')

class MinHeap:
    
    heap: list[T] = []
    
    # Constructor to initialize heap with elements
    def __init__(self, elements: list[T]) -> None:
        self.heap = elements
    
    # Insert an element and maintain heap property
    def push(self, value: T):
        self.heap.append(value)  # Append element at end
        idx = len(self.heap) - 1
        parent = (idx - 1) >> 1  # Parent index

        # Swap with parent while new element is smaller
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) >> 1

    # Maintain heap structure starting from index i
    def heapify(self, n: int, i: int):
        smallest = i
        left_child = (i << 1) + 1  # Left child index
        right_child = (i << 1) + 2  # Right child index

        # Check if left child is smaller than current smallest
        if left_child < n and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        # Check if right child is smaller than current smallest
        if right_child < n and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        # Swap and heapify the subtree if needed
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(n, smallest)

    # Build min heap from array
    def create_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):  # Start from last non-leaf node
            self.heapify(n, i)

    # Retrieve root element (smallest element in min heap)
    def peek(self) -> T:
        return self.heap[0] if self.heap else None

    # Remove and return the root element
    def pop(self) -> T:
        if len(self.heap) == 0:
            return None
        self.heap[0] = self.heap[-1]  # Replace root with last element
        self.heap.pop()  # Remove last element
        self.heapify(len(self.heap), 0)  # Restore heap property


if __name__ == '__main__':
    
    # BUILD MIN HEAP EXAMPLES
    elements = [9, 5, 15, 3, 7, 8]
    heap = MinHeap(elements)
    heap.create_heap()
    print(f'Heap after building: {heap.heap}')
    # Output: [3, 5, 8, 9, 7, 15]
    
    elements = [9.2, 5.5, 15.1, 3.3, 7.7, 8.8]
    heap = MinHeap(elements)
    heap.create_heap()
    print(f'Heap after building (floats): {heap.heap}')
    # Output: [3.3, 5.5, 8.8, 9.2, 7.7, 15.1]

    elements = [1012345678901234567, 999999999999999999, 1234567890123456789, 555555555555555555]
    heap = MinHeap(elements)
    heap.create_heap()
    print(f'Heap after building (long integers): {heap.heap}')
    # Output: [555555555555555555, 999999999999999999, 1234567890123456789, 1012345678901234567]

    elements = [25, 12, 18, 9, 5, 3]
    heap = MinHeap(elements)
    heap.create_heap()
    print(f'Heap after building: {heap.heap}')
    # Output: [3, 5, 18, 9, 12, 25]
    
    # INSERT EXAMPLES
    heap.push(2)
    print(f'Heap after inserting 2: {heap.heap}')
    # Output: [2, 5, 3, 9, 12, 25, 18]

    heap.push(6)
    print(f'Heap after inserting 6: {heap.heap}')
    # Output: [2, 5, 3, 6, 12, 25, 18, 9]
    
    # POP EXAMPLES
    heap.pop()
    print(f'Heap after popping root: {heap.heap}')
    # Output: [3, 5, 9, 6, 12, 25, 18]

    heap.pop()
    print(f'Heap after popping root: {heap.heap}')
    # Output: [5, 6, 9, 18, 12, 25]
    
    # GET ROOT EXAMPLE
    elements = [18, 5, 9, 3, 12, 25]
    heap = MinHeap(elements)
    heap.create_heap()
    print(f'Heap: {heap.heap}')
    print(f'Root element: {heap.peek()}')
    # Output: Heap: [3, 5, 9, 18, 12, 25]
    #         Root element: 3
