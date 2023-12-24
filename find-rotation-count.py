# Write a function called findRotationCount 
# which accepts an array of distinct numbers sorted in increasing order. 
# The array has been rotated counter-clockwise n number of times. 
# Given such an array, find the value of n

def findRotationCount(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # If the array is already sorted, no rotation
        if arr[left] < arr[right]:
            return left

        mid = (left + right) // 2

        # Check if mid is the smallest element
        if arr[mid] < arr[mid - 1]:
            return mid

        # Determine which side to continue the search
        if arr[mid] > arr[left]:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example usage
arr = [15, 18, 2, 3, 6, 12]
print(findRotationCount(arr))  # Output: 2, as the array is rotated 2 times

