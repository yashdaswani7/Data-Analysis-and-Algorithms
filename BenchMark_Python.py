# Author Information
# Name: Yash Daswani
# ID: 1002257766


import time
import random
import matplotlib.pyplot as plt


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = 0
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = 1
        if not swapped:
            break

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value

# Benchmark each sorting algorithm
def benchmark_sorting_algorithm(sort_function, sizes):
    total_time = []
    for size in sizes:
        arr = [random.randint(-23000, 23000) for _ in range(size)]
        start_time = time.time()
        sort_function(arr)
        end_time = time.time()
        total_time.append(end_time - start_time)
    return total_time


# Define test sizes
test_sizes = [10, 50, 100, 500, 1000, 2000, 7000, 21000, 33000 ]

# Run benchmarks
selection_times = benchmark_sorting_algorithm(selection_sort, test_sizes)
bubble_times = benchmark_sorting_algorithm(bubble_sort, test_sizes)
insertion_times = benchmark_sorting_algorithm(insertion_sort, test_sizes)

# Plot results
plt.figure(figsize=(12, 8))
plt.plot(test_sizes, selection_times, label="Selection Sort", marker='o')
plt.plot(test_sizes, bubble_times, label="Bubble Sort", marker='x')
plt.plot(test_sizes, insertion_times, label="Insertion Sort", marker='^')

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Benchmarking Sorting Algorithms")
plt.legend()
plt.grid(True)
plt.show()