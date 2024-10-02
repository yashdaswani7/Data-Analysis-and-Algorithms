import sys
import time
import random
import matplotlib.pyplot as plt

# Increase recursion limit
sys.setrecursionlimit(10000000)

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

# Benchmarking quicksort
def benchmark_quicksort(arr):
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Best-case scenario: already sorted
def generate_best_case(size):
    return list(range(size))

# Worst-case scenario: reverse sorted
def generate_worst_case(size):
    return list(range(size, 0, -1))

# Average-case scenario: random values
def generate_average_case(size):
    return [random.randint(0, size) for _ in range(size)]

# Run benchmark tests
def run_benchmarks():
    input_sizes = [100, 200, 500, 1000, 2000, 5000, 7000, 9000]  
    best_case_times = []
    worst_case_times = []
    average_case_times = []

    # Running benchmarks for each input size
    for size in input_sizes:
        # Best case (sorted input)
        best_case_input = generate_best_case(size)
        best_case_times.append(benchmark_quicksort(best_case_input.copy()))

        # Worst case (reverse sorted input)
        worst_case_input = generate_worst_case(size)
        worst_case_times.append(benchmark_quicksort(worst_case_input.copy()))

        # Average case (random input)
        average_case_input = generate_average_case(size)
        average_case_times.append(benchmark_quicksort(average_case_input.copy()))

    # Plotting the results
    plt.plot(input_sizes, best_case_times, label="Best Case (Sorted Input)", marker="o")
    plt.plot(input_sizes, worst_case_times, label="Worst Case (Reverse Sorted Input)", marker="o")
    plt.plot(input_sizes, average_case_times, label="Average Case (Random Input)", marker="o")

    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Performance for Non-Random Pivot')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_benchmarks()
