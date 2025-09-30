def selection_sort(arr):
    """Sorts an array in ascending order using selection sort."""
    # Iterate through the entire array
    for i in range(len(arr)):
        # Assume the current position has the minimum value
        min_index = i
        
        # Find the minimum element in the remaining unsorted portion
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numbers)
selection_sort(numbers)
print("Sorted:", numbers)
