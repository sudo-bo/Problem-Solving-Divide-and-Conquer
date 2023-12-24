def countZeroes(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == 0:
            if mid == 0 or arr[mid - 1] == 1:
                return len(arr) - mid
            else:
                right = mid - 1
        else:
            left = mid + 1
    return 0

