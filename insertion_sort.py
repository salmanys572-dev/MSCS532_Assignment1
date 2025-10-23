# Author: 
# Course: MSCS 532 - Assignment 1
# Description: Insertion Sort algorithm that sorts a list in decreasing order

def insertion_sort_descending(arr):
    """
    This function sorts an array in monotonically decreasing order
    using the Insertion Sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements that are smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key


# Example array for testing
if __name__ == "__main__":
    data = [12, 4, 56, 17, 8, 99, 5, 23]
    print("Original Array:", data)
    
    insertion_sort_descending(data)
    
    print("Sorted Array (Decreasing Order):", data)

# Insertion Sort in Decreasing Order
# Step through the array and insert each element into the correct position

# Additional test case
data2 = [45, 2, 19, 78, 33]
insertion_sort_descending(data2)
print("Sorted Array 2:", data2)


