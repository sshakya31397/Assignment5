def quicksort(arr):
    # Base case: If the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Select a pivot. Here, we use the last element as the pivot.
    pivot = arr[-1]
    
    # Partitioning step: Split the array into elements less than the pivot, 
    # elements equal to the pivot, and elements greater than the pivot
    less_than_pivot = [x for x in arr[:-1] if x < pivot]
    greater_than_pivot = [x for x in arr[:-1] if x >= pivot]
    
    # Recursively apply quicksort to the subarrays and concatenate the results
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Example usage:
arr = [10, 7, 8, 9, 1, 5, 22, 11, 99, 3, 55, 2, 44]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)