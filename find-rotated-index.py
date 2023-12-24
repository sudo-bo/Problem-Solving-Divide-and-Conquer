# Write a function called findRotatedIndex 
# which accepts a rotated array of sorted numbers and an integer. 
# ([6, 7, 8, 9, 1, 2, 3, 4], 8)
# The function should return the index of num in the array. 
# If the value is not found, return -1.

# def findRotatedIndex(rotated_arr, target):
#     left = 0
#     right = findHighest(rotated_arr)
#     if target > rotated_arr[right]:
#         left = right
#         right = len(rotated_arr) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if rotated_arr[mid] > target:
#                 left = mid + 1
#             elif rotated_arr[mid] < target:
#                 right = mid - 1
#             elif rotated_arr[mid] == target:
#                 return mid 
#         return -1

# def findHighest(arr):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] > arr[left]:
#             left = mid + 1
#         elif arr[mid] < arr[left]:
#             right = mid - 1
#         elif arr[mid] == arr[left]:
#             left = mid
#     return left 
# [ 9 1 ]

def findRotatedIndex(rotated_arr, target):
    def findPivot(arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        return left

    def binarySearch(arr, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    pivot = findPivot(rotated_arr)

    if target == rotated_arr[pivot]:
        return pivot
    elif target >= rotated_arr[0]:
        return binarySearch(rotated_arr, 0, pivot - 1, target)
    else:
        return binarySearch(rotated_arr, pivot, len(rotated_arr) - 1, target)

# Example usage
index = findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8)
print(index)  # Output should be the index of 8 in the array
