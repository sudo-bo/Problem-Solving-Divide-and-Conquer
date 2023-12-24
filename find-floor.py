# Write a function called findFloor which accepts 
# a sorted array and a value x, and returns the floor of x in the array. 
# The floor of x in an array is the largest element in the array 
# which is smaller than or equal to x. If the floor does not exist, return -1.

# def findFloor(arr, x):
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if arr[left] == x or arr[right] == x:
#             return x
#         elif arr[left] > x:
#             return -1
        
#         if arr[mid] < x:
#             if arr[mid + 1] >= x:
#                 return arr[mid + 1]
#             left = mid + 1
#         elif arr[mid] > x:
#             if arr[mid - 1] <= x:
#                 return arr[mid - 1]
#             right = mid - 1
#         else:
#             return arr[mid]

def findFloor(arr, x):
    left, right = 0, len(arr) - 1
    floor = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            floor = arr[mid]
            left = mid + 1
        else:
            right = mid - 1
    return floor

# Example usage
arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
print(findFloor(arr, x))  # Output should be 2, which is the floor of 5 in the array

