import time
import random

# Iterative Deterministic Quicksort (pivot as the last element)
def deterministic_quicksort(arr):
    stack = [(0, len(arr) - 1)]  # Stack to hold (low, high) pairs

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))  # Left partition
            stack.append((pivot_index + 1, high))  # Right partition

# Iterative Randomized Quicksort (choosing pivot randomly)
def randomized_quicksort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = random_partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

# Partition function using Lomuto partitioning
def partition(arr, low, high):
    pivot = arr[high]  # Last element as pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Move pivot to correct position
    return i + 1

# Randomized partition function
def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap random pivot with last element
    return partition(arr, low, high)

# Function to measure runtime for sorting algorithms
def measure_runtime(algorithm, arr):
    arr_copy = arr[:]  # Create a copy to avoid modifying the original
    start_time = time.time()
    algorithm(arr_copy)  
    return time.time() - start_time

# Function to run the experiment on different input distributions
def run_experiment():
    sizes = [100, 1000, 5000, 10000]  # Different input sizes
    input_types = ['random', 'sorted', 'reverse_sorted']
    results = {}

    for size in sizes:
        for input_type in input_types:
            # Generate input arrays
            if input_type == 'random':
                arr = random.sample(range(size * 2), size)
            elif input_type == 'sorted':
                arr = list(range(size))
            elif input_type == 'reverse_sorted':
                arr = list(range(size, 0, -1))

            # Measure runtime of deterministic and randomized quicksort
            deterministic_time = measure_runtime(deterministic_quicksort, arr)
            randomized_time = measure_runtime(randomized_quicksort, arr)

            results[(size, input_type)] = (deterministic_time, randomized_time)

    return results

# Running the experiment
experiment_results = run_experiment()

# Output results
for (size, input_type), (det_time, rand_time) in experiment_results.items():
    print(f"Size: {size}, Type: {input_type}")
    print(f"Deterministic Quicksort Time: {det_time:.6f}s")
    print(f"Randomized Quicksort Time: {rand_time:.6f}s")
    print("-" * 40)
